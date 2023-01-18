import unittest
from login.verification import *

class VerificationTest(unittest.TestCase):
    #check if fname is too short
    def test_checkFname_short_lower(self):
        fname = ""
        check = checkFName(fname)
        self.assertEqual(check, 2, "Should throw error code 2")

    #check if fname length is on lower boundary
    def test_checkFname_short_boundary(self):
        fname = "a"
        check = checkFName(fname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if fname is too long
    def test_checkFname_long_upper(self):
        fname = "qwertyuiopasdfghj"
        check = checkFName(fname)
        self.assertEqual(check, 1, "Should throw error code 1")

    #check if fname length is on upper boundary
    def test_checkFname_long_boundary(self):
        fname = "qwertyuiopasdfgh"
        check = checkFName(fname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if fname length is within boundary
    def test_checkFname_in_boundary(self):
        fname = "qwerty"
        check = checkFName(fname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if fname has special characters
    def test_checkFname_special_char(self):
        fname = "qwerty%"
        check = checkFName(fname)
        self.assertEqual(check, 3, "Should throw error code 3")

    #checks special case "name"
    def test_checkFname_name(self):
        fname = "name"
        check = checkFName(fname)
        self.assertEqual(check, 4, "Should succeed and return with code 4")

#------------------------------------------------------------------------------------------

    #check if surname is too short
    def test_checkSurname_short_lower(self):
        surname = ""
        check = checkSurname(surname)
        self.assertEqual(check, 2, "Should throw error code 2")

    #check if surname length is on lower boundary
    def test_checkSurname_short_boundary(self):
        surname = "a"
        check = checkSurname(surname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if surname is too long
    def test_checkSurname_long_upper(self):
        surname = "qwertyuiopasdfghjklzxcvbnmqwertyu"
        check = checkSurname(surname)
        self.assertEqual(check, 1, "Should throw error code 1")

    #check if surname length is on upper boundary
    def test_checkSurname_long_boundary(self):
        surname = "qwertyuiopasdfghjklzxcvbnmqwerty"
        check = checkSurname(surname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if surname length is within boundary
    def test_checkSurname_in_boundary(self):
        surname = "qwerty"
        check = checkSurname(surname)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if surname has special characters
    def test_checkSurname_special_char(self):
        surname = "qwerty%"
        check = checkSurname(surname)
        self.assertEqual(check, 3, "Should throw error code 3")

#------------------------------------------------------------------------------------------

    #check if email is too short
    def test_checkEmail_short_lower(self):
        email = "a@b"
        check = checkEmail(email)
        self.assertEqual(check, 2, "Should throw error code 2")

    #check if email length is on lower boundary
    def test_checkEmail_short_boundary(self):
        email = "a@b.c"
        check = checkEmail(email)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if email is too long
    def test_checkEmail_long_upper(self):
        email = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxc@"
        check = checkEmail(email)
        self.assertEqual(check, 1, "Should throw error code 1")

    #check if email length is on upper boundary
    def test_checkEmail_long_boundary(self):
        email = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzx@"
        check = checkEmail(email)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if email length is within boundary
    def test_checkEmail_in_boundary(self):
        email = "qwerty@mail.com"
        check = checkEmail(email)
        self.assertEqual(check, 0, "Should succeed and return with code 0")

    #check if email has special characters
    def test_checkEmail_special_char(self):
        email = "qwerty%@"
        check = checkEmail(email)
        self.assertEqual(check, 3, "Should throw error code 3")

    #check if email does not contain @
    def test_checkEmail_at(self):
        email = "qwerty"
        check = checkEmail(email)
        self.assertEqual(check, 4, "Should throw error code 4")