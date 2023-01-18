#App Configurations
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()

#Sizes
WIDTH_MAIN = screen.size().width()
HEIGHT_MAIN = screen.size().height()
TOAST_MAIN = int(WIDTH_MAIN/2) -100

LEFT_HEADER = int(WIDTH_MAIN/5)
TOP_HEADER = int(HEIGHT_MAIN/25)
WIDTH_HEADER = int(3*WIDTH_MAIN/5)
HEIGHT_HEADER = int(HEIGHT_MAIN/8)
TOP_HEADER_SHADOW = int(TOP_HEADER + HEIGHT_HEADER/10)

LEFT_SEARCH = int(WIDTH_MAIN/5)
TOP_SEARCH = int(HEIGHT_MAIN/6)
WIDTH_SEARCH = int(3*WIDTH_MAIN/5)
HEIGHT_SEARCH = int(HEIGHT_MAIN/25)

HLAYOUT_HEIGHT = int(HEIGHT_MAIN/20)
HLAYOUT_WIDTH = int(WIDTH_MAIN/5)
HLAYOUT_LEFT = WIDTH_MAIN-HLAYOUT_WIDTH-100
HLAYOUT_TOP = 0
HLAYOUT_SPACING = 20

WIDTH_SUB = int(WIDTH_MAIN/4)
HEIGHT_SUB = int(HEIGHT_MAIN/2.5)
LEFT_SUB = int(WIDTH_MAIN/2 - WIDTH_SUB/2)
TOP_SUB = int(HEIGHT_MAIN/4)
BOTTOM_LOGIN = int(HEIGHT_MAIN/3)

MARGIN_SUB_VBOX = int(WIDTH_SUB/4)
HEIGHT_SUB_VBOX = int(HEIGHT_SUB/6)
WIDTH_SUB_VBOX = int(WIDTH_SUB/2)
TOP_SUB_VBOX = int(HEIGHT_SUB/10)

MARGIN_BUTTON = int(WIDTH_SUB/8)

WIDTH_GRID = int(3*WIDTH_MAIN/5)
HEIGHT_GRID = int(4*HEIGHT_MAIN/5 - 100)
LEFT_GRID = int(WIDTH_MAIN/5)
TOP_GRID = int(HEIGHT_MAIN/5 + 50)

MAX_HEIGHT_ITEM = 400

WIDTH_DEP= int(WIDTH_MAIN/7)
HEIGHT_DEP = int(4*HEIGHT_MAIN/10)
LEFT_DEP = int(WIDTH_MAIN/24)
TOP_DEP = int(HEIGHT_MAIN/6)

WIDTH_CART_WINDOW =int(2*WIDTH_MAIN/3)
HEIGHT_CART_WINDOW =int(2*HEIGHT_MAIN/3)
TOP_CART_WINDOW=int(HEIGHT_MAIN/6)
LEFT_CART_WINDOW=int(WIDTH_MAIN/6)
MARGIN_CART_WINDOW_SIDES=150
MARGIN_CART_WINDOW_BOTTOM=50

MAX_HEIGHT_ITEM_CART = 150
HEIGHT_CART_BOX=int(4*HEIGHT_CART_WINDOW/5 - 70)
WIDTH_CART_BOX=int(4*WIDTH_CART_WINDOW/5)
LEFT_CART_BOX=MARGIN_CART_WINDOW_SIDES
TOP_CART_BOX=int(HEIGHT_CART_WINDOW/5 +20)

WIDTH_CHECKOUT_BOX =int(WIDTH_CART_BOX/4)
HEIGHT_CHECKOUT_BOX = int(HEIGHT_CART_WINDOW/10)
WIDTH_CHECKOUT_BUTTON = int(28*WIDTH_CHECKOUT_BOX/30)
HEIGHT_CHECKOUT_BUTTON = int(2*HEIGHT_CHECKOUT_BOX/5)

GENERAL_MARGIN = 20

#Color pallette
DARK_PINK = QColor(221, 4, 89)      #0xdd0459
PINK = QColor(235, 104, 150)        #0xeb6896
SOFT_PINK = QColor(253, 153, 167)   #0xfd99a7
YELLOW = QColor(251, 251, 143)      #0xfbfb8f
WHITE = QColor(238, 238, 238)       #0xeeeeee
BLACK = QColor(7, 10, 13)           #0x070a0d

#Images
HEADER_TITLE = "./icons/header_title.png"
LOGIN_TITLE = "./icons/login_title.png"
REGISTER_TITLE = "./icons/register_title.png"
CART_TITLE = "./icons/cart_title.png"
WISHLIST_TITLE = "./icons/wishlist_title.png"
DETAILS_TITLE = "./icons/details_title.png"
CHECKOUT_TITLE = "./icons/checkout_title.png"
ACCOUNT_TITLE = "./icons/account_title.png"
SEARCH = "./icons/search.png"
BALL = "./icons/ball.png"
BOOK = "./icons/book.png"
CART = "./icons/cart.png"
MOUSE = "./icons/mouse.png"
SHIRT = "./icons/shirt.png"
SOAP = "./icons/soap.png"
USER = "./icons/user.png"
WISHLIST = "./icons/wishlist2.png"
BIN = "./icons/bin.png"

#Provinces
PROVINCES = ["Eastern Cape", "Free State", "Gauteng", 
            "KwaZulu-Natal", "Limpopo", "Mpumalanga",
            "Northern Cape", "North West", "Western Cape"]