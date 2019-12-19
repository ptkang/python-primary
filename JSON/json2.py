'''
@Author: your name
@Date: 2019-11-30 22:20:55
@LastEditTime: 2019-11-30 23:26:50
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

# 序列化 将Python数据类型向其他类型的字符串转换的过程

# NOSQL数据库 MongoDB
# JavaScript: 实现ECMASCRIPT的语言之一
# ActionScript
# TypeScript

# JSON对象: JavaScript的一种JSON概念 
# JSON: 实现ECMASCRIPT的一种语言
# JSON字符串

# REST服务的标准格式：建议用JSON格式

import json

student = [
            {'name': 'qiyue', 'age': 18, 'flag': False},
            {'name': 'justin', 'age': 20}
          ]

json_array = json.dumps(student)
print(json_array)
print(type(json_array))