# -*- coding: utf-8 -*-
'''
@Author: your name
@Date: 2019-11-29 21:29:50
@LastEditTime: 2019-11-30 20:58:38
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
# . 匹配出换行符\n之外的所有字符

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
# 6. 组()，()里面的字符是一个且关系，将()里面的字符串当做一个整体，来用数量词将组里面的整体匹配若干次
# 7. 集[]，[]里面的字符是一个或关系，将[]里面的任意一个字符来用数量词修饰匹配

# 匹配模式参数
#   re.I 忽略大小写
#   re.S 是的.可以匹配任意一个字符，包括换行符\n

# 正则表达式函数
# import re
# re.findall
# re.sub

import re

language = 'PythonC#JavaC#PHPC#'
#language = 'PythonC#JavaPHP'

def convert(value):
    print(value)
    #print(value.__dict__)
    print(type(value))
    #print(re.Match.__dict__)
    print('value.start()=', value.start())
    print('value.end()=', value.end())
    print('value.span()=', value.span())
    print('value.groups()=', value.groups())
    print('value.groupdict()=', value.groupdict())
    #print('value.expand()=', value.expand())
    print('value.string=', value.string)
    print('value.re=', value.re)
    print('value.pos=', value.pos)
    print('value.endpos=', value.endpos)
    print('value.lastindex=', value.lastindex)
    print('value.lastgroup=', value.lastgroup)
    print('value.regs=', value.regs)
    return '!!' + value.group() + '!!'

r = re.sub('C#', convert, language, 0)
print(r)