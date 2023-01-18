from PyQt5 import QtCore, QtQuickWidgets
from PyQt5.QtGui import QFont
from configurations import *

class QToaster(QtWidgets.QFrame):
    closed = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QToaster, self).__init__(*args, **kwargs)
        QtWidgets.QHBoxLayout(self)

        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, 
                           QtWidgets.QSizePolicy.Maximum)

        self.setStyleSheet('''
            QToaster {
                border: 1px solid black;
                border-radius: 4px; 
                '''
                "background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + ");}"
        )

        self.timer = QtCore.QTimer(singleShot=True, timeout=self.hide)

        if self.parent():
            self.opacityEffect = QtWidgets.QGraphicsOpacityEffect(opacity=0)
            self.setGraphicsEffect(self.opacityEffect)
            self.opacityAni = QtCore.QPropertyAnimation(self.opacityEffect, b'opacity')
            # we have a parent, install an eventFilter so that when it's resized
            # the notification will be correctly moved to the centre bottom
            self.parent().installEventFilter(self)
        else:
            # there's no parent, use the window opacity property, assuming that
            # the window manager supports it; if it doesn't, this won'd do
            # anything (besides making the hiding a bit longer by half a second)
            self.opacityAni = QtCore.QPropertyAnimation(self, b'windowOpacity')
        self.opacityAni.setStartValue(0.)
        self.opacityAni.setEndValue(1.)
        self.opacityAni.setDuration(100)
        self.opacityAni.finished.connect(self.checkClosed)

        self.myWindow = kwargs.get('myWindow', TOAST_MAIN)
        self.margin = 10
        self.bottom = kwargs.get('bottom', self.margin)

    def checkClosed(self):
        # if we have been fading out, we're closing the notification
        if self.opacityAni.direction() == self.opacityAni.Backward:
            self.close()

    def restore(self):
        # this is a "helper function", that can be called from mouseEnterEvent
        # and when the parent widget is resized. We will not close the
        # notification if the mouse is in or the parent is resized
        self.timer.stop()
        # also, stop the animation if it's fading out...
        self.opacityAni.stop()
        # ...and restore the opacity
        if self.parent():
            self.opacityEffect.setOpacity(1)
        else:
            self.setWindowOpacity(1)

    def hide(self):
        # start hiding
        self.opacityAni.setDirection(self.opacityAni.Backward)
        self.opacityAni.setDuration(500)
        self.opacityAni.start()

    def eventFilter(self, source, event):
        if source == self.parent() and event.type() == QtCore.QEvent.Resize:
            self.opacityAni.stop()
            parentRect = self.parent().rect()
            geo = self.geometry()
            geo.moveBottomLeft(parentRect.bottomLeft() + QtCore.QPoint(self.myWindow, -self.margin))
            self.setGeometry(geo)
            self.restore()
            self.timer.start()
        return super(QToaster, self).eventFilter(source, event)

    def enterEvent(self, event):
        self.restore()

    def leaveEvent(self, event):
        self.timer.start()

    def closeEvent(self, event):
        # we don't need the notification anymore, delete it!
        self.deleteLater()

    @staticmethod
    def showMessage(parent, message, 
                    icon=QtWidgets.QStyle.SP_MessageBoxInformation, 
                    myWindow=TOAST_MAIN, margin=10, closable=True,
                    timeout=1500, parentWindow=True, bottom=10):
        
        if parent and parentWindow:
            parent = parent.window()

        if bottom != 10:
            margin = bottom
        
        self = QToaster(parent)
        parentRect = parent.rect()

        self.timer.setInterval(timeout)

        # use Qt standard icon pixmaps; see:
        # https://doc.qt.io/qt-5/qstyle.html#StandardPixmap-enum
        if isinstance(icon, QtWidgets.QStyle.StandardPixmap):
            labelIcon = QtWidgets.QLabel()
            self.layout().addWidget(labelIcon)
            icon = self.style().standardIcon(icon)
            size = self.style().pixelMetric(QtWidgets.QStyle.PM_SmallIconSize)
            labelIcon.setPixmap(icon.pixmap(size))
            labelIcon.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + ");")
           
        self.label = QtWidgets.QLabel(message)
        self.label.setFont(QFont('AnyStyle', 12))
        self.label.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + ");")
        self.layout().addWidget(self.label)

        if closable:
            self.closeButton = QtWidgets.QToolButton()
            self.closeButton.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + ");")
            self.layout().addWidget(self.closeButton)
            closeIcon = self.style().standardIcon(
                QtWidgets.QStyle.SP_TitleBarCloseButton)
            self.closeButton.setIcon(closeIcon)
            self.closeButton.setAutoRaise(True)
            self.closeButton.clicked.connect(self.close)

        self.timer.start()

        # raise the widget and adjust its size to the minimum
        self.raise_()
        self.adjustSize()

        self.myWindow = myWindow
        self.margin = margin

        geo = self.geometry()
        # now the widget should have the correct size hints, let's move it to the
        # right place
        geo.moveBottomLeft(parentRect.bottomLeft() + QtCore.QPoint(myWindow, -margin))
        self.setGeometry(geo)
        self.show()
        self.opacityAni.start()