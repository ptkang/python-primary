'''
@Author: your name
@Date: 2019-12-10 21:27:11
@LastEditTime: 2019-12-10 22:12:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\pythonic\iterator_generator1.py
'''
# 列表、元组、集合不是迭代器
# 可迭代对象、迭代器
# 迭代器是一个对象class，可以被for in 循环迭代
# for in iterable iterator
# 只要一个类里面实现了__iter__和__next__函数，则这个类可以被迭代器迭代
# 我们可以用一个迭代器使用next,但不能对列表，元组，集合使用迭代器，因其不是迭代器
# 迭代器只能遍历1次，即具有一次性特性，这个和列表，元组，集合有区别
# 要再次遍历迭代器，只能再实例化一个新的对象，或使用对象的拷贝

# 生成器对应一个函数

n = [i for i in range(1, 101)] # n是一个list，数据量太大会十分耗内存
print(type(n))
n = (i for i in range(1, 101)) # n是一个generator，相当于保存一个算法
print(type(n))
for i in n:
    print(i)

'''
def gen(max):
    n = 1
    while n < max:
        yield n
        n += 1

n = gen(101)
print(type(n))

for i in n:
    print(i)
'''