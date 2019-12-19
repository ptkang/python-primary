'''
@Author: your name
@Date: 2019-11-30 22:20:55
@LastEditTime: 2019-11-30 23:02:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\JSON\json1.py
'''
# JSON: JavaScript Object Notation, JavaScript对象标记
#       是一种轻量级的数据交换格式
#       字符串是JSON的表现形式
# JSON字符串：符合JSON格式的字符串
# JSON特点：
#   1. 易于阅读
#   2. 易于解析         跨语言交换数据
#   3. 网络传输效率高
# 典型应用场景： 网站后台==>浏览器
# 反序列化： 由字符串到python语言的某一种类型
# json                  python
# object                dict
# array                 list
# string                str
# number                int
# number                flot
# true                  True
# false                 False
# null                  None

import json

json_str = '{"name":"qiyue", "age":18}'
json_array = '[{"name":"qiyue", "age":18, "flag":false},{"name":"justin", "age":20}]'

student1 = json.loads(json_str)
print(student1)
#print('name=' + student['name'])
#print('age=' + str(student['age']))
student2 = json.loads(json_array)
print(student2)
print("student2[0]['name']=", student2[0]['name'])