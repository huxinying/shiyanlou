# -*-coding:utf-8-*-

import os, sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
'''
current_path = os.path.abspath(os.path.dirname(__file__))
shiyanlou_path = os.path.join(current_path, os.path.pardir, os.path.pardir)
test_path = os.path.join(current_path, os.path.pardir)
sys.path.append(shiyanlou_path)
sys.path.append(test_path)

from utils.ReadConfig import ReadConfig
from test.common.PageMenuOperation import PageMenuOperation
from test.common.PagingOperation import PagingOperation
from selenium.webdriver.common.keys import Keys

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

    def page_menu_operation(self, menu=[]):
        """页面菜单选择"""
        return PageMenuOperation(self.driver).select_menu(menu)

    def paging_operation(self, page):
        """分页操作"""
        return PagingOperation(self.driver).paging_operation(page)

class BootcampPage(BasePage):
    """训练营页面"""
    def __search_element(self):
        # 打开登录窗口按钮
        return self.find_element("form input[placeholder='搜索 课程/问答")

    def search(self, text):
        """检索功能"""
        sleep(3)
        self.__search_element().clear()
        self.__search_element().send_keys(text)
        # 发送 “回车键”
        self.__search_element().send_keys(Keys.ENTER)

if __name__ == '__main__':
    #page = BasePage()
    #page.page_menu_operation(["训练营"])
    # page.close_page()
    bootcamp = BootcampPage(url='https://www.shiyanlou.com/bootcamp/')
    bootcamp.search(123)
    # bootcamp.close_page()