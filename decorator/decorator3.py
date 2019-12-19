'''
@Author: your name
@Date: 2019-12-07 22:51:24
@LastEditTime: 2019-12-07 23:36:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\decorator\decorator1.py
'''
# 装饰器
# 开闭原则：对修改式封闭的，对扩展式开放的
# 可以接受定义时候的复杂，决不能接受调用时候的复杂
import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(name):
    #print(time.time())
    print('This is a function1' + name)

@decorator
def f2(name1, name2):
    #print(time.time())
    print('This is a function2' + name1 + name2)

# 将扩展需求在本质上并没有与原先调用关联起来
f1('Justin')

# 保持了原先的调用逻辑
f2('ptkang', 'King')