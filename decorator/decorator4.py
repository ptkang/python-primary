'''
@Author: your name
@Date: 2019-12-07 22:51:24
@LastEditTime: 2019-12-07 23:50:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\decorator\decorator1.py
'''
# 装饰器
# 开闭原则：对修改式封闭的，对扩展式开放的
# 可以接受定义时候的复杂，决不能接受调用时候的复杂
import time

def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(name):
    #print(time.time())
    print('This is a function1' + name)

@decorator
def f2(name1, name2):
    #print(time.time())
    print('This is a function2' + name1 + name2)

@decorator
def f3(name1, name2, **kw):
    #print(time.time())
    print('This is a function2' + name1 + name2)
    for key, value in kw.items():
        print(key + ':' + str(value))

#def f4(**kw, name1, name2):
    #print(time.time())
#    print('This is a function2' + name1 + name2)
#    for key, value in kw.items():
#        print(key + ':' + str(value))

f1('Justin')
f2('ptkang', 'King')
f3('ptkang', 'King', bj='36c', shanghai=38)
#f4(bj='36c', shanghai=38, name1='ptkang', name2='King')
f3(bj='36c', shanghai=38, name1='ptkang', name2='King')