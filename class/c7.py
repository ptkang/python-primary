'''
@Author: your name
@Date: 2019-11-26 22:16:44
@LastEditTime: 2019-11-29 00:05:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\class\c1.py
'''
# 面向对象
# 写出有意义的面向对象的代码
# 类最基本的作用是封装代码（变量+函数）
# 面向对象三大特性：封装性，继承性，多态性
class Human():
    sum = 0
    name = '石敢当'
    age = 21
    gender = '女'
    def __init__(self, name, age, gender):
        #self.__name = name
        self.name = name
        self.__age = age
        self.__gender = gender

    def print_human_doc(self):
        #print('name: ' + str(self.__name) + ' age: ' + str(self.__age) + ' gender: ' + str(self.__gender))
        print('name: ' + str(self.name) + ' age: ' + str(self.__age) + ' gender: ' + str(self.__gender))
        self.print_Human_doc()

    @classmethod
    def print_Human_doc(cls):
        print('name: ' + str(cls.name) + ' age: ' + str(cls.age) + ' gender: ' + str(cls.gender))

    def do_homowork(self):
        print("do Person %s's homework" % self.name)