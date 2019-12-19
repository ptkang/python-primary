'''
@Author: your name
@Date: 2019-12-10 22:56:24
@LastEditTime: 2019-12-10 23:06:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\decorator.py
'''
# 装饰器的负作用
#

import time
from functools import wraps

def decorator(func):
    @wraps(func)
    def wraper(*args, **kw):
        print(time.time())
        func()
    return wraper

@decorator
def f1():
    '''
        This is f1
    '''
    print('This is f1')
    print(f1.__name__)

f1()
print(help(f1))