import unittest
from cart import *

testCart = currCart()
testWish = currWishList()

class DatabaseTest(unittest.TestCase):
    #adding to cart works
    def test_AddCart_success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        check = testCart.add_item(item)
        self.assertEqual(check, 0, "Should throw error code 0")
        testCart.remove_item(1)
    #adding to cart fails
    def test_AddCart_failure(self):
        item = [1, 'Adidas Bag', 649.94]
        check = testCart.add_item(item)
        self.assertEqual(check, 1, "Should throw error code 1")
    #removing from cart works
    def test_DelCart_Success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        testCart.add_item(item)
        check = testCart.remove_item(1)
        self.assertEqual(check, 0, "Should throw error code 0")
    #removing from cart fails
    def test_DelCart_Failure(self):
        check = testCart.remove_item(0)
        self.assertEqual(check, 1, "Should throw error code 1")
    #testing calc total works
    def test_calcTotal_Success(self):
        check = testCart.calc_total()
        self.assertEqual(check, 0, "Should throw error code 0")
    #testing calc total fails
    def test_calcTotal_Failure(self):
        item = [1, 'Adidas Bag', '649.94', 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        testCart.add_item(item)
        check = testCart.calc_total()
        self.assertEqual(check, 1, "Should throw error code 1")
        testCart.remove_item(1)
    #getting item from cart works
    def test_getItem_success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        testCart.add_item(item)
        check = testCart.get_item(item[0])[0]
        self.assertEqual(check, 1, "Should return ID==1")
        testCart.remove_item(1)
    #getting item from cart fails
    def test_getItem_failure(self):
        check = testCart.get_item(1)
        self.assertEqual(check, 1, "Should throw error code 1")

    #adding to wishlist works
    def test_AddWL_success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        check = testWish.add_item(item)
        self.assertEqual(check, 0, "Should throw error code 0")
        testWish.remove_item(1)
    #adding to wishlist fails
    def test_AddWL_failure(self):
        item = [1, 'Adidas Bag', 649.94]
        check = testWish.add_item(item)
        self.assertEqual(check, 1, "Should throw error code 1")
    #removing from wishlist works   
    def test_DelWL_Success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        testWish.add_item(item)
        check = testWish.remove_item(1)
        self.assertEqual(check, 0, "Should throw error code 0")
    #removing from wishlist fails   
    def test_DelWL_Failure(self):
        check = testWish.remove_item(1)
        self.assertEqual(check, 1, "Should throw error code 1")
    #getting item from wishlist works
    def test_getItem_wishlist_success(self):
        item = [1, 'Adidas Bag', 649.94, 'RilAsh@gmail.com', 'Sports', './products/bag.png']
        testWish.add_item(item)
        check = testWish.get_item(item[0])[0]
        self.assertEqual(check, 1, "Should return ID==1")
        testCart.remove_item(1)
    #getting item from wishlist fails
    def test_getItem_wishlist_failure(self):
        check = testWish.get_item(1)
        self.assertEqual(check, 1, "Should throw error code 1")