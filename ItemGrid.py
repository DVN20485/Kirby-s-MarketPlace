from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configurations import *
from database import *
from cart import *
import math

class itemGrid(QWidget):
    def __init__(self, parentWindow): #parentWidnow is the mainWindow object to be passed as a parameter 
      super ().__init__()
      self.parentWindow = parentWindow
      self.allProducts = {}
      self.row = 0
      self.column = 0
      self.addGrid()

    def addGrid(self): 
      self.allProducts = getProductList()
      height_grid_scroll = int(math.ceil(len(self.allProducts)/3)) * MAX_HEIGHT_ITEM

      self.GridWidget = QWidget(self.parentWindow) #grid to contain vertical layouts
      self.GridWidget.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID-20, height_grid_scroll))
      self.GridWidget.setObjectName("GridWidget")
      self.GridWidget.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 4px; border-style: outset;")
      self.Grid = QGridLayout(self.GridWidget)
      self.Grid.setObjectName("Grid")

      self.scrollArea = QScrollArea(self.parentWindow) #scrollable grid
      self.scrollArea.setStyleSheet("background-color: rgb(" + str(PINK.red()) + "," + str(PINK.green()) + "," + str(PINK.blue()) + "); padding: 8px; border-style: outset;")
      self.scrollArea.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID, HEIGHT_GRID))
      self.scrollArea.setWidget(self.GridWidget)
      self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
      self.parentWindow.roundCorners(10.0, self.scrollArea)
      
      if(self.allProducts!=-1):
        for myProduct in self.allProducts:
          self.addNewItem(myProduct)
          self.row+=1
          if(self.row==3):
            self.column+=1
            self.row=0

    def addNewItem(self, item):
      def addToCart(event):
        myCart.add_item(item)

      def addToWishlist(event):
        myWishlist.add_item(item)

      vItemBoxWidget = QWidget(self.GridWidget) #vertical layout to store item info
      vItemBoxWidget.setObjectName("vItemBoxWidget")
      vItemBoxWidget.setStyleSheet("background-color: rgb(" + str(SOFT_PINK.red()) + "," + str(SOFT_PINK.green()) + "," + str(SOFT_PINK.blue()) + "); padding: 4px; border-style: outset;")
      vItemBoxWidget.setMaximumHeight(MAX_HEIGHT_ITEM)
      vItemBox = QVBoxLayout(vItemBoxWidget)
      vItemBox.setObjectName("vItemBox")
      self.Grid.addWidget(vItemBoxWidget, self.column, self.row)

      #name tag
      hDetailsLayoutWidget = QWidget(self)
      hDetailsLayoutWidget.setObjectName("hDetailsLayoutWidget")
      hDetailsLayout = QHBoxLayout(hDetailsLayoutWidget)
      hDetailsLayout.setObjectName("hDetailsLayout")
      vItemBox.addWidget(hDetailsLayoutWidget)

      lblName = QLabel(item[1], self)
      lblName.setAlignment(Qt.AlignCenter)
      lblName.setFont(QFont('AnyStyle', 14))
      hDetailsLayout.addWidget(lblName)

      #price
      lblPrice = QLabel("R" + str(item[2]), self)
      lblPrice.setAlignment(Qt.AlignCenter)
      lblPrice.setFont(QFont('AnyStyle', 14))
      hDetailsLayout.addWidget(lblPrice)

      #image
      mainImage = QPixmap(item[5])
      lblProduct = QLabel(self)
      lblProduct.setAlignment(Qt.AlignCenter)
      lblProduct.setPixmap(mainImage)
      lblProduct.setScaledContents(True)
      vItemBox.addWidget(lblProduct)

      #wishlist and carts
      hWishLayoutWidget = QWidget(self)
      hWishLayoutWidget.setObjectName("hWishLayoutWidget")
      hWishLayout = QHBoxLayout(hWishLayoutWidget)
      hWishLayout.setObjectName("hWishLayout")
      vItemBox.addWidget(hWishLayoutWidget)

      lblCart = QLabel(hWishLayoutWidget)
      lblCart.setPixmap(QPixmap(CART))
      lblCart.setAlignment(Qt.AlignCenter)
      lblCart.mousePressEvent = addToCart
      lblCart.setCursor(Qt.PointingHandCursor)
      hWishLayout.addWidget(lblCart)
      
      lblWish = QLabel(hWishLayoutWidget)
      lblWish.setPixmap(QPixmap(WISHLIST))
      lblWish.setAlignment(Qt.AlignCenter)
      lblWish.mousePressEvent = addToWishlist
      lblWish.setCursor(Qt.PointingHandCursor)
      hWishLayout.addWidget(lblWish)

    def sortBy(self, department):
      for i in reversed(range(self.Grid.count())): 
        self.Grid.itemAt(i).widget().setParent(None)

      self.row = 0
      self.column = 0

      self.allProducts = categoryList(department)
      height_grid_scroll = int(math.ceil(len(self.allProducts)/3)) * MAX_HEIGHT_ITEM
      self.GridWidget.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID-20, height_grid_scroll))

      if(self.allProducts!=-1):
        for myProduct in self.allProducts:
          self.addNewItem(myProduct)
          self.row+=1
          if(self.row==3):
            self.column+=1
            self.row=0
    def searchBy(self, name):
      for i in reversed(range(self.Grid.count())): 
        self.Grid.itemAt(i).widget().setParent(None)

      self.row = 0
      self.column = 0

      self.allProducts = search(name)
      height_grid_scroll = int(math.ceil(len(self.allProducts)/3)) * MAX_HEIGHT_ITEM
      self.GridWidget.setGeometry(QRect(LEFT_GRID, TOP_GRID, WIDTH_GRID-20, height_grid_scroll))

      if(self.allProducts!=-1):
        for myProduct in self.allProducts:
          self.addNewItem(myProduct)
          self.row+=1
          if(self.row==3):
            self.column+=1
            self.row=0