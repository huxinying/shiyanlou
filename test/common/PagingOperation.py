# -*-coding:utf-8-*-

from time import sleep
from selenium.webdriver.common.by import By


class PagingOperation(object):
    """分页操作"""
    def __init__(self, driver):
        sleep(1)
        self.driver = driver
        # 分页整体定位
        self.__paging = self.driver.find_element(By.CLASS_NAME, 'number-pagination')
        # 页数
        self.__pageing_number = self.__paging.find_elements(By.CSS_SELECTOR, '.page-link')

    def __get_page(self, text):
        """获取分页"""
        # 使翻页区域可见
        self.driver.execute_script("arguments[0].scrollIntoView(false);", self.__paging)
        sleep(3)

        try:
            if text == "上一页":
                return self.__pageing_number[0]
            elif text == "下一页":
                return self.__pageing_number[-1]
            else:
                for paging_number in self.__pageing_number:
                    if paging_number.text == str(text):
                        return paging_number
        except:
            error = "只接收上一页、下一页和页面可见的整型数字"
            print(error)
            return

    def paging_operation(self, text):
        """分页操作"""
        if self.__get_page(text):
            self.__get_page(text).click()

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.shiyanlou.com/bootcamp/')

    paging = PagingOperation(driver)
    paging.paging_operation(3)
    #paging.paging_operation("上一页")
    #paging.paging_operation("下一页")
    paging.paging_operation(123)

    # driver.quit()