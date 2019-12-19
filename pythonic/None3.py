'''
@Author: your name
@Date: 2019-12-10 22:13:07
@LastEditTime: 2019-12-10 22:52:37
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

# 0, '', (), [], {}, None对应False
# __len__只能返回整形integer或True或False
# __bool__只能返回bool类型，不能返回如0等其他类型
# 对一个对象：
#   1.若__bool__函数自定义的话，bool(对象)的返回结果由__len__函数返回结果决定，否则由__bool__函数返回结果决定
#   2.bool函数和len函数都会调用对象的__len__函数
#   3.若一个对象没有私有的__len__函数，对一个对象调用len(对象)会报错

class Test1():
    pass

test1 = Test1()

if test1:
    print('S')
else:
    print('N')

# 对象存在不一定为真True
class Test2():
    # 强制让对象的为False
    def __bool__(self):
        return False
    # 强制让对象的长度为0
    def __len__(self):
        return 0

test2 = Test2()

class Test3():
    # 强制让对象的为True
    def __bool__(self):
        return True
    # 强制让对象的长度为0
    def __len__(self):
        return 0

test3 = Test3()

class Test4():
    # 强制让对象的为True
    def __bool__(self):
        return False
    # 强制让对象的长度为0
    def __len__(self):
        return 1

test4 = Test4()

class Test5():
    # 强制让对象的为True
    def __bool__(self):
        return True
    # 强制让对象的长度为0
    def __len__(self):
        return False

test5 = Test5()

if test2:
    print('S')
else:
    print('N')

print(bool(0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(test1))
print(bool(test2))
print(bool(test3))
print(bool(test4))
print(bool(test5))