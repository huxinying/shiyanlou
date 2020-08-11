# -*-coding:utf-8-*-

"""
Created on 2020-06-06
Project: 实验楼自动化测试
@Author: Tynam
"""

import sys, os

current_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_path)
from test.runner.main import Main


if __name__ == '__main__':
    Main().run_case()