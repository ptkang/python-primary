'''
@Author: your name
@Date: 2019-12-10 22:13:07
@LastEditTime: 2019-12-10 22:25:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\\None.py
'''

# None 空
# None 无从类型还是屈指，都不等于空字符串、空的列表、0、False
# 判空操作2中操作方法：
# 1. if a
# 2. if not a

# None 和 False区别
# None：表示不存在，False表示真假
# None和False类型不同

def func():
    return None

#a = func()
a = ''

if not a:
    print('S')
else:
    print('N')

if a == None:
    print('S')
else:
    print('N')