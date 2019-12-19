'''
@Author: your name
@Date: 2019-11-26 22:16:44
@LastEditTime: 2019-11-26 23:43:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\class\c1.py
'''
# 面向对象
# 写出有意义的面向对象的代码
# 类最基本的作用是封装代码（变量+函数）
class Student():
    name = '石敢当'
    age = 21
    gender = '女'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_student_doc(self):
        print('name: ' + str(self.name) + ' age: ' + str(self.age) + ' gender: ' + str(self.gender))

student = Student('Justin', 34, '男')
student.print_student_doc()
print('name: ' + str(student.name) + ' age: ' + str(student.age) + ' gender: ' + str(student.gender))
print('name: ' + str(Student.name) + ' age: ' + str(Student.age) + ' gender: ' + str(Student.gender))