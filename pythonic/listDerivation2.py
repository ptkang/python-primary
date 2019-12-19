'''
@Author: your name
@Date: 2019-12-10 20:49:55
@LastEditTime: 2019-12-10 22:02:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\switchcase.py
'''
# 列表推导式：根据一个已经存在的列表推导一个新的列表
# set，dict, tuple也可以被推导

students = {
    '喜小乐': 18,
    '石敢当': 20,
    '横小五': 15
}

b = [key for key, value in students.items()]
print(b)

c = {value:key for key, value in students.items()}
print(c)

d = (key for key, value in students.items()) # d编程一个生成器generator
print(type(d))
for x in d:
    print(x)

e = [key for key, value in students.items()]
print(e)
