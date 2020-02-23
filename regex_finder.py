#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
    chapter 8.9.3 正则表达式查找
    编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。 
    regex_finder
"""

import os, re
import  cpp_cutter

def regex_finder(regex):
    # txt file all together
    ls_txt = []
    for item in os.listdir():
        #当前目录中所有txt后缀的文件
        item = str(item).split('.')
        if len(item) > 1 and item[1] == 'txt':
            ls_txt.append('.'.join(item))
            #记录txt文件名
    # print(ls_txt)
    Regex = re.compile(regex)
    num = 0
    for file in ls_txt:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        for line in content:
            match = Regex.search(line)
            if match != None:
                print(line)
                num += 1
    print('共计',num,'条')

if __name__ == '__main__':
    cpp_cutter.cutter()

    # regex = input('please input a regex: ')
    # regex = r'第.*条'
    # regex_finder(regex)



# TODO 高频词分析
# TODO 特征提取



