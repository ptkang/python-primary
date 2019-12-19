'''
@Author: your name
@Date: 2019-12-07 22:51:24
@LastEditTime: 2019-12-07 23:05:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\decorator\decorator1.py
'''
# 装饰器
# 开闭原则：对修改式封闭的，对扩展式开放的
import time

def f1():
    #print(time.time())
    print('This is a function1')

def f2():
    #print(time.time())
    print('This is a function2')

def print_curtime(func):
    print(time.time())
    func()

print_curtime(f1)
print_curtime(f2)