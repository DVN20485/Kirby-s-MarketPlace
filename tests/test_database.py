from getpass import getuser
from locale import getpreferredencoding
import unittest
from database import *

class DatabaseTest(unittest.TestCase):
    #registration testing
    def test_Register_success(self):
        check = register("name", "surname", "email", "password", "salt")
        self.assertEqual(check, 0, "Should throw error code 0")
    def test_Register_fail(self):
        check = register("name", "surname", "reg@mail.com", "password", "salt")
        self.assertEqual(check, 1, "Should throw error code 1")
    #login testing
    def test_Login_success(self):
        check = login("reg@mail.com", "1234")
        self.assertEqual(check, 0, "Should throw error code 0")  
    def test_Login_FailMismatch(self):
        check = login("reg@mail.com", "123")
        self.assertEqual(check, 1, "Should throw error code 1")
        
    #User info testing
    def test_getInfo(self):
        check = getUserInfo("reg@mail.com")
        self.assertEqual(check, ('register', 
        'tests', 'reg@mail.com', 
        '4cdacfddbf05f958ad6d93740ac38116d36018da3f15245ed066ee31f658b72de49401e320d3476873217b451324c60aea539ccbee447f3ab66f50ef2cc06bab', 
        '37fa8e0cad5040bdb78f49ef773592fa'), "Should wrong info given")
    def test_getInfoNull(self):
        check = getUserInfo("")
        self.assertEqual(check, "User does not exist", "Should wrong info given")

    def test_getSalt(self):
        check = getSalt("reg@mail.com")
        self.assertEqual(check, '37fa8e0cad5040bdb78f49ef773592fa', "Should wrong info given")
    def test_getSaltNull(self):
        check = getSalt("")
        self.assertEqual(check, -1, "Should wrong info given")
    #Product testing   
    def test_addremoveProduct(self):
        check = addProduct("Infinity Edge", 0, "ProductEmail", "productCat", "productPAth")
        self.assertEqual(check, 0, "should throw code 0")
        
    def test_prodList(self):
        a = getProductList()
        check = len(a)
        self.assertEqual(check, 21, "Length should be 21")
        
    def test_catList(self):
        a = categoryList("Sports")
        check = len(a)
        self.assertEqual(check, 5, "Length should be 5")  
        
    #Order testing
    def test_addOrder(self):
        check = addOrder("Infinity Edge", 0, "", "CellNo", "Province", "Address", "Postcode", "imgPath")
        self.assertEqual(check, 0, "should throw code 0")
        
    def test_orderList(self):
        check = userOrders("reg@mail.com")[0][0]
        self.assertEqual(check, 1, "Order No should be 1")  
        
    def test_Search(self):
        check = search("Crocs")[0][1]
        self.assertEqual(check, "Crocs", "Order No should be 1")
        
    
    


