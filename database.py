import sqlite3
from login.encrypter import encrypt
from login.verification import checkFName

connection = sqlite3.connect('KirbysDatabase.db')
#============================================================================================

def register(fname, surname, email, password, salt):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (fname, surname, email, password, salt)) #attempt registration
    except:
        return 1

    nameCheck = checkFName(fname) #if fname is "name" pass test but dont commit
    if(nameCheck==4):
        return 0
    if(fname != "name"):
        connection.commit()
        return 0
    #return 0 on registration success, 1 if there was an error
    

#============================================================================================

def login(email, password): #take in user info
    cursor = connection.cursor()
    salt=getSalt(email)
    snhpassword, salt = encrypt(password, salt=salt)
    try:
        cursor.execute("SELECT Password FROM Users WHERE Email = ?", (email,))
        pas = cursor.fetchall()[0][0]
        if (pas == snhpassword): #attempt make sure password is matching
            return 0
        else:
            return 1
    except:
        return -1
        #return 0 if login success, 1 if details entered were incorrect and -1 if external error

#============================================================================================

def getUserInfo(email): #jsut takes in email and returns a list containing the users information in order name,surname,email,password
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
    temp = cursor.fetchall()
    if temp != []:
        UserList = temp[0]
    else:
        return "User does not exist"

    return UserList

#============================================================================================

def getSalt(email): #Gets salt to compare passwords
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT Salt FROM Users WHERE Email = ?", (email,))
        #cursor.execute("UPDATE Users SET Salt= 'de0b36567fca446c863f9c3d78162b11', Password= '14bfa65071cd794b5203284be0e048511169a20caa6e375b4791e2cce8d000f2ec1891b53a2288e32cea64dd2ebfb4cce487f9463a4e98ce1f488e9c58131401' WHERE Email='test@mail.com';")
        #connection.commit()
        salt = cursor.fetchall()[0][0]
        return salt
    except:
        print("There was an external error")
        return -1
    
#============================================================================================

def getProductList():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall() #return a  full list of every product in the database
    except:
        print("There was an external error")
        return -1

def addProduct(ProductName, ProductPrice, ProductEmail, ProductCategory, imagePath): #adds a product to the database, auto increments and sets the ID
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Products (ProductName, ProductPrice, ProductOwner, ProductCategory, imagePath ) VALUES (?, ?, ?, ?, ?)", (ProductName, ProductPrice, ProductEmail, ProductCategory, imagePath))
    except:
        return 1
    if (ProductName != "Infinity Edge"):
        connection.commit()
    return 0

def removeProduct(productID): #removes item from the databse using only the ID since the ID is unique to each product
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Products WHERE ProductID = ?", (productID,))
    except:
        return 1
    connection.commit()
    return 0

def categoryList(category):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE ProductCategory = ?", (category,))
    return cursor.fetchall()

#=====================================================================================================================
#Orders 

def addOrder(ProductName, ProductPrice, UserEmail, CellNo, Province, Address, Postcode, imgPath): #adds an order to the database of orders
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Orders (ProductName, ProductPrice, UserEmail, CellNo, Province, Address, Postcode, imgPath) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (ProductName, ProductPrice, UserEmail, CellNo, Province, Address, Postcode, imgPath))
    except:
        print("Failed")
        return 1
    if (ProductName != "Infinity Edge"):
        connection.commit()
    #connection.commit()
    return 0

def userOrders(userEmail): #returns the list of orders a user has ade
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders WHERE UserEmail = ?", (userEmail,))
    return cursor.fetchall()

#search

def search(ProductName):
    cursor = connection.cursor()
    s = "%" + ProductName + "%"
    cursor.execute("SELECT * FROM Products WHERE ProductName LIKE ?", (s,))
    return cursor.fetchall()