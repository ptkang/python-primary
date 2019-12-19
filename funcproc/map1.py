'''
@Author: your name
@Date: 2019-12-07 21:13:58
@LastEditTime: 2019-12-07 22:49:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\funcproc\Lambada1.py
'''
# 匿名函数
# lambada表达式
# lambda parameter_list: expression
# 三元表达式
# 条件为真时返回的结果 if 判断条件 else 条件为假时的返回结果
# r = x if x > y else y
# map 通过一个函数将一个列表映射到另一个列表
#     lambada表达式引入几个变量，后面必须有几个对应的列表
#     map的结果数量取决于最短列表的数量
#     map返回的是一个map类，需要用list函数转换为列表
# reduce 连续计算，连续调用lambda
# map/reduce编程模型: 映射/规约 并行计算
# filter 过滤

# 命令式编程要素: 函数def、条件判断if、循环for
# 函数式编程要素: map, reduce, filter lambda(算子)

from functools import reduce
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 4, 9, 16, 25, 36, 49, 64]
def square(x):
    return x ** 2

r = map(square, list_x)
print(r)
print(list(r))

r = map(lambda x: x ** 2, list_x)
print(list(r))

r = map(lambda x, y: x ** 2 + y, list_x, list_y)
print(list(r))

list_z = [1, 4, 9, 16, 25, 36]
r = map(lambda x, y: x ** 2 + y, list_x, list_z)
print(list(r))

r = reduce(lambda x, y: x + y, list_x)
print(r)

list_a = [1, 0, 1, 0, 0, 1]
r = filter(lambda x: True if x == 1 else False, list_a)
print(list(r))

#r = filter(lambda x: 2 if x == 1 else 3, list_a)
#print(list(r))

r = filter(lambda x: 1 if x == 1 else 0, list_a)
print(list(r))

r = filter(lambda x: x, list_a)
print(list(r))

list_u = ['a', 'B', 'c', 'F', 'e']
r = filter(lambda c: True if c >= 'a' else False, list_u)
print(list(r))