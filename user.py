import database
from cart import *

class currUser:
    def __init__(self, **kwargs): #this is called after users login has been verified
        self.email = kwargs.get('email', 0)
        if(self.email!=0):
            userInfo = database.getUserInfo(self.email)
            self.fName = userInfo[0]
            self.surname = userInfo[1]
            self.password = userInfo[3]
        else:
            self.email = "test@mail.com"
            self.fName = "Test"
            self.surname = "Account"
            self.password = "6969"

        self.Inventory = [] #this will later be use to store the items the user is selling
        self.cart = myCart #users cart
        self.wishlist = myWishlist #users wishlist

    def Login(self, email):
        userInfo = database.getUserInfo(email)
        self.fName = userInfo[0]
        self.surname = userInfo[1]
        self.password = userInfo[3]

    def get_Name(self):
        return self.fName

    def get_Surname(self):
        return self.surname

    def get_Email(self):
        return self.email

myUser=currUser()