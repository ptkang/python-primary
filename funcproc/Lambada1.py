'''
@Author: your name
@Date: 2019-12-07 21:13:58
@LastEditTime: 2019-12-07 21:37:25
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

def add(x, y):
    return x + y

print(add(1,2))

f = lambda x,y: x+y
print(f(1,2))

x = 2
y = 1
r = x if x > y else y
print(r)