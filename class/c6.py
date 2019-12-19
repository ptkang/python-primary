'''
@Author: your name
@Date: 2019-11-26 22:16:44
@LastEditTime: 2019-11-29 00:06:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\class\c1.py
'''
# 面向对象
# 写出有意义的面向对象的代码
# 类最基本的作用是封装代码（变量+函数）
# 面向对象三大特性：封装性，继承性，多态性
from c7 import Human
class Student(Human):
    def __init__(self, school, name, age, gender):
        self.school = school
        #Human.__init__(self, name, age, gender)
        super(Student, self).__init__(name, age, gender)

    def do_homowork(self):
        #print("do Student %s's homework" % super(Student, self).__name)
        print("do Student %s's homework" % self.name)
        super(Student, self).do_homowork()

student = Student('人民路小学', 'Justin', 34, '男')
student.print_human_doc()
student.do_homowork()