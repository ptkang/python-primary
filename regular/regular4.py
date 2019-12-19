# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2019-11-29 21:29:50
@LastEditTime: 2019-11-29 23:37:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\regular\regular2.py
'''
# 正则表达式
# JSON(XML)

# 正则表达式是一个特殊的字符序列，一个字符串是否与我们所设定的
# 这样的字符序列相匹配
# 正则表达式的灵魂在于规则
# 
# 快速检索文本、实现一些替换文本的操作
# 
# 1. 检查一串数字是否是电话号码
# 2. 检测一个字符串是否符合email
# 3. 把一个文本里指定的单词替换为另外一个单词

# 概括字符集
# \d 数字字符 \D 非数字字符
# \w 单词字符 \W 非单词字符
# \s 空白字符 \S 非空白字符

# 1. 数量词 {m, n}
#   贪婪和非贪婪
#   贪婪模式{m,n}
#   非贪婪模式{m,n}?
# 2. * 匹配前面的字符0次或无限多次
# 3. + 匹配前面的字符1次或无限多次
# 4. ? 匹配前面的字符0次或1次, 用于去重复字符
# 5. 边界匹配
#    ^ 从字符串开头开始匹配
#    $ 从字符串末尾开始匹配

import re

print("re.findall('\d{4,8}', '101')=", re.findall('\d{4,8}', '101'))
print("re.findall('\d{4,8}', '100001')=", re.findall('\d{4,8}', '100001'))
print("re.findall('\d{4,8}', '100000001')=", re.findall('\d{4,8}', '100000001'))
print("re.findall('^\d{4,8}$', '100000001')=", re.findall('^\d{4,8}$', '100000001'))
print("re.findall('^000', '100000001')=", re.findall('^000', '100000001'))
print("re.findall('000$', '100000001')=", re.findall('000$', '100000001'))