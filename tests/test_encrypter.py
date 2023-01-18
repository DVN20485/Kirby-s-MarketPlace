import unittest
from login.encrypter import *
import numpy.random as np

class EncrypterTest(unittest.TestCase):
    #Test if generates new salt without kwargs
    def test_encrypt_no_kwargs_salt(self):
        salt = encrypt("6969")
        salt2 = encrypt("6969")
        self.assertNotEqual(salt, salt2, "Should generate new salt")

    #Test generates same password from given salt
    def test_encrypt_password_with_given_salt(self):
        snhpass, salt = encrypt("6969", salt="de0b36567fca446c863f9c3d78162b11")
        self.assertEqual(snhpass, "14bfa65071cd794b5203284be0e048511169a20caa6e375b4791e2cce8d000f2ec1891b53a2288e32cea64dd2ebfb4cce487f9463a4e98ce1f488e9c58131401", "Did not generate same password")

    #Test if generates new salt without kwargs
    def test_encrypt_password_with_random_salt(self):
        password = str(np.randint(1000, 10000))
        snhpass, salt = encrypt(password)
        snhpass2, salt2 = encrypt(password, salt=salt)
        self.assertEqual(snhpass, snhpass2, "Should encrypt password the same twice")