# -*-coding:utf-8-*-

import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path = os.path.abspath(os.path.dirname(__file__))
shiyanlou_path = os.path.join(current_path, os.path.pardir, os.path.pardir)
sys.path.append(shiyanlou_path)
from utils.ReadConfig import ReadConfig


class BasePage(object):
    """基础页面"""

    def __init__(self, browser='Chrome', driver_path=None, url=None):
        """
        基础的参数，browser、webdriver、默认访问的 url
        :param browser: 浏览器
        :param driver_path: 浏览器驱动
        :param url: 默认打开的 url，一般都是实验楼首页
        """

        if driver_path is None:
            driver_path = os.path.join(shiyanlou_path, 'drivers/chromedriver')

        if url is None:
            data = ReadConfig().read_json()
            url = data['base_url']
            self.base_url = url
        else:
            self.base_url = url

        if browser == "Chrome":
            self.driver = webdriver.Chrome(driver_path)
        else:
            print("请输入支持的浏览器")

        # 默认打开实验楼首页
        self.open_page()

    def open_page(self):
        """打开默认页面"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()

    def find_element(self, element, by=By.CSS_SELECTOR):
        """返回单个定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, element, by=By.CSS_SELECTOR):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.find_elements(by, element)

if __name__ == '__main__':
    page = BasePage()

    # page.close_page()