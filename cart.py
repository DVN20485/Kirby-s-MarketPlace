class currCart:
    def __init__(self):
        self.cartList = {} #list of cart items in a dictionary with their price. Eg: cartlist["sword"] = 420.10
        self.totalCost = 0.00 #total sum of the price of items within the disctionary
        
    #add item usng its ID price and name
    def add_item(self, item):
        try:   
            self.cartList[item[0]] = [item[0],item[1], item[2], item[3], item[4], item[5]] #ID, Name, Price, Seller, Department, imagePath
            self.calc_total()
            return 0
        except:
            return 1
    #remove item usng its ID
    def remove_item(self, itemID):
        try:
            del self.cartList[itemID]
            self.calc_total()
            return 0
        except:
            return 1
    #keep track of the sum of the users cart when theyre using the application, its updated everytime they add or remove an item automatically  
    def calc_total(self):
        sum = 0
        try:
            for x in self.cartList:
                sum += self.cartList[x][2]
            self.totalCost = sum
            return 0
        except:
            return 1
    #get item from ID
    def get_item(self, itemID):
        try:   
            return self.cartList[itemID]
        except:
            return 1

class currWishList:
    def __init__(self):
        self.wishlist = {} #list of cart items in a dictionary with their price. Eg: cartlist["sword"] = 420.10
    #add item usng its ID price and naem    
    def add_item(self, item):
        try:
            self.wishlist[item[0]] = [item[0], item[1], item[2], item[3], item[4], item[5]] #ID, Name, Price, Seller, Department, imagePath
            return 0
        except:
            return 1
    #remove item usng its ID
    def remove_item(self, itemID):
        try:
            del self.wishlist[itemID]
            return 0
        except:
            return 1
    #get item from ID
    def get_item(self, itemID):
        try:   
            return self.wishlist[itemID]
        except:
            return 1

myCart = currCart()
myWishlist = currWishList()