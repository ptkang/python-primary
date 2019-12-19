# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2019-11-29 21:29:50
@LastEditTime: 2019-11-29 22:48:19
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

import re
a = 'C1 C++2#Java\t3C#&4Python5\n_\rJavascript'

# print(a.index('Python') > -1)

# print('Python' in a)

print('数字字符=', re.findall('\d', a))
print('非数字字符=', re.findall('\D', a))
print('单词字符=', re.findall('\w', a))
print('非单词字符=', re.findall('\W', a))
print('空白字符=', re.findall('\s', a))
print('非空白字符=', re.findall('\S', a))