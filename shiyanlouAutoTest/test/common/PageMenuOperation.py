# -*-coding:utf-8-*-

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PageMenuOperation(object):
    """页面菜单操作"""
    def __init__(self, driver):
        sleep(1)
        self.driver = driver

        # 菜单导航
        self.__menu = self.driver.find_element(By.CSS_SELECTOR, '#nav-collapse ul[class="navbar-nav base-menu"]')
        # 第一层菜单
        self.__first_nav = self.__menu.find_elements(By.CSS_SELECTOR, '.nav-item a, .base-menu-dropdown button')
        # 第二层菜单
        self.__second_nav = self.__menu.find_elements(By.CSS_SELECTOR, 'a.dropdown-item')

    def __get_first_menu(self, text):
        """获取第一层菜单"""
        for fist_menu in self.__first_nav:
            if fist_menu.text == text:
                return fist_menu

    def __get_second_menu(self, text):
        """获取第二层菜单"""
        for second_menu in self.__second_nav:
            if second_menu.text == text:
                return second_menu

    def select_menu(self, menu_text=[]):
        try:
            if len(menu_text) == 1:
                menu = menu_text[0]
                self.__get_first_menu(menu).click()
            elif len(menu_text) == 2:
                first_menu = menu_text[0]
                second_menu = menu_text[1]
                # 鼠标悬停第一层菜单元素
                ActionChains(self.driver).move_to_element(self.__get_first_menu(first_menu)).perform()
                self.__get_second_menu(second_menu).click()

            else:
                err = "列表参数中只能有一个或两个值"
                print(err)
                return
        except:
            err = "所输入的菜单名称未找到"
            print(err)
            return

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.shiyanlou.com/louplus/')

    PageMenu = PageMenuOperation(driver)
    PageMenu.select_menu(["训练营"])
    PageMenu.select_menu(["社区", "直播"])

    #driver.quit()