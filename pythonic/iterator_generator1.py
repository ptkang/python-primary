'''
@Author: your name
@Date: 2019-12-10 21:27:11
@LastEditTime: 2019-12-10 21:51:43
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

import copy

class Book:
    pass

class BookCollection:
    def __init__(self):
        self.data = ['<往事>', '<只能>', '<回味>']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r;

books = BookCollection()
books_copy = copy.copy(books) #copy.copy是浅拷贝,copy.deepcopy是深拷贝

#print(next(books))
#print(next(books))
#print(next(books))
#print(next(books)) # StopIteration
for book in books:
    print(book)

#books_copy = copy.copy(books) 放这儿没有用
for book in books_copy:
    print(book)