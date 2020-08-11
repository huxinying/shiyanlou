# -*-coding:utf-8-*-

import os, sys
from time import sleep
from selenium.webdriver.common.by import By

from test.pages.basePage import BasePage

current_path = os.path.abspath(os.path.dirname(__file__))
shiyanlou_path = os.path.join(current_path, os.path.pardir, os.path.pardir)
sys.path.append(shiyanlou_path)
sys.path.append(current_path)
from utils.ReadConfig import ReadConfig



class LoginPage(BasePage):
    """登录功能页面"""

    def __open_login_page_element(self):
        # 打开登录窗口按钮
        return self.find_element('li.sign-in-btn')

    def __phone_element(self):
        # 账号
        return self.find_element("input[placeholder='手机号/邮箱")

    def __password_element(self):
        # 密码
        return self.find_element("input[placeholder='密码']")

    def __login_button_element(self):
        # 登录按钮
        return self.find_element("button.ant-btn-primary")

    def __get_account(self):
        """获取默认的登录账号和密码"""
        data = ReadConfig().read_json()
        phone = data['phone']
        password = data['password']
        return phone, password

    def open_login_page(self):
        """打开登录弹窗"""
        return self.__open_login_page_element().click()

    def login(self, phone=None, password=None):
        """登录"""
        # 获取配置文件账号和密码
        default_phone, default_password = self.__get_account()

        if phone is None:
            phone = default_phone
        if password is None:
            password = default_password

        self.__phone_element().clear()
        self.__phone_element().send_keys(phone)
        self.__password_element().clear()
        self.__password_element().send_keys(password)
        self.__login_button_element().click()

if __name__ == '__main__':
    login = LoginPage()
    login.open_login_page()
    login.login()
    # login.close_page()