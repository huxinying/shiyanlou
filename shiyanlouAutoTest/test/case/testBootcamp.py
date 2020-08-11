# -*-coding:utf-8-*-

import os, sys
import unittest

from test.pages.bootcampPage import BootcampPage

current_path = os.path.abspath(os.path.dirname(__file__))
test_path = os.path.join(current_path, os.path.pardir)
sys.path.append(test_path)


class TestBootcamp(unittest.TestCase):
    """训练营测试用例"""

    @classmethod
    def setUpClass(cls):
        cls.bootcamp = BootcampPage(url='https://www.lanqiao.cn/bootcamp/')

    @classmethod
    def tearDownClass(cls):
        cls.bootcamp.quit_driver()

    def test_bootcamp_001(self):
        self.bootcamp.paging_operation(3)
        self.bootcamp.paging_operation("上一页")
        self.bootcamp.paging_operation("下一页")

    def test_bootcamp_002(self):
        self.bootcamp.search('测试')

    def test_bootcamp_003(self):
        self.bootcamp.page_menu_operation(["社区", "直播"])

if __name__ == '__main__':
    unittest.main()