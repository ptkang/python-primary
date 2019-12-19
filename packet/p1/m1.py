'''
@Author: your name
@Date: 2019-11-24 14:09:28
@LastEditTime: 2019-11-24 23:10:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\+vscode\p1\m1.py
'''
import sys
import os
sys.path.append(os.getcwd()+'/../')
print("sys.path=", sys.path)

from m2 import m2
import p2
from p11.m11 import m11
print("m11=", m11)
#print(__version__)
print("hello world:%s-%s"%("ptkang", "Justin"))
print("m11=%d"%m11)
print("hello word:%s"%"ptkang")
print("__annotations__=",__annotations__)
print("__builtins__=",__builtins__)
print("__cached__=",__cached__)
print("__doc__=",__doc__)
print("__file__=",__file__)
print("__loader__=",__loader__)
print("__name__=",__name__)
print("__package__=",__package__);
print("__spec__=",__spec__)
print("dir()=",dir())
print("os.getcwd()=",os.getcwd())