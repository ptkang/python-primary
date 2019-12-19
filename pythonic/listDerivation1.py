'''
@Author: your name
@Date: 2019-12-10 20:49:55
@LastEditTime: 2019-12-10 21:19:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\switchcase.py
'''
# 列表推导式：根据一个已经存在的列表推导一个新的列表
# set，dict, tuple也可以被推导

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i ** 2 for i in a if i >= 5]
print(b)

c = {1, 2, 3, 4, 5, 6, 7, 8}
d = {i ** 2 for i in c if i >= 5}
print(d)