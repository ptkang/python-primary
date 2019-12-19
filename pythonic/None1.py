'''
@Author: your name
@Date: 2019-12-10 22:13:07
@LastEditTime: 2019-12-10 22:17:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\\None.py
'''

# None 空
# None 无从类型还是屈指，都不等于空字符串、空的列表、0、False
# 

a = ''
b = False
c = []

print(a == None)
print(b == None)
print(c == None)

print(a is None)
print(b is None)
print(c is None)

print(type(None)) # <class 'NoneType'>