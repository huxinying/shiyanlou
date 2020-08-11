# -*-coding:utf-8-*-

import os, sys
import unittest
from time import sleep

from test.pages.loginPage import LoginPage

current_path = os.path.abspath(os.path.dirname(__file__))
test_path = os.path.join(current_path, os.path.pardir)
sys.path.append(test_path)



class TestLogin(unittest.TestCase):
    """登录测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_login_001(self):
        self.login.open_login_page()
        self.login.login()

    def test_login_002(self):
        self.login.login(phone='123445', password='3333333')

if __name__ == '__main__':
    unittest.main()