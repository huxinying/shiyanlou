# -*-coding:utf-8-*-

import os
import json


class ReadConfig(object):
    """
    读取配置文件，Excel、josn 等文件的读取方法都可写在此类下
    """
    def __init__(self):
        pass

    def read_json(self, json_file=None):
        """读取json文件"""

        # 设置默认文件
        if json_file is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            json_file = os.path.join(current_path, os.path.pardir, 'config/base_data.json')

        try:
            with open(json_file) as f:
                data = json.load(f)
                return data
        except:
            print("文件不存在或不是json文件")

if __name__ == '__main__':
    data = ReadConfig().read_json()
    print(data)
    print(data['base_url'], data['phone'], data['password'])