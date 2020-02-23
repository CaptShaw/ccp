#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
    cpp cutter
"""
import os, re

def cutter():
    # to cut ccp.txt apart
    #http://www.12371.cn/special/zggcdzc/zggcdzcqw/
    with open('ccp.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    titleRegex = re.compile('总.*纲|第.{1,2}章.*')
    order = []
    for line in content:
        #非None即匹配成功
        if titleRegex.search(line) != None:
            order += [content.index(line)]
            #记录标题所在行号

    for o in range(len(order)):
        if o < len(order) - 1 :
            chapter = content[order[o]:order[o+1]]
            #避免o+1造成溢出
        elif o == len(order) - 1 :
            chapter = content[order[o]:]
        # title = re.compile('\s').sub('',str(content[order[o]]))
        # title = str(content[order[o]]).strip()
        title = str(content[order[o]].strip()) + '.txt'
        with open(title, 'w+', encoding='utf-8') as f:
            f.write(''.join(chapter))

if __name__ == '__main__':
    cutter()