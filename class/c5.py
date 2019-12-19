'''
@Author: your name
@Date: 2019-11-26 22:16:44
@LastEditTime: 2019-11-28 23:02:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\class\c1.py
'''
# 面向对象
# 写出有意义的面向对象的代码
# 类最基本的作用是封装代码（变量+函数）
class Student():
    __name = '石敢当'
    __age = 21
    __gender = '女'
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def print_student_doc(self):
        print('name: ' + str(self.__name) + ' age: ' + str(self.__age) + ' gender: ' + str(self.__gender))
        #print('name: ' + str(Student.__name) + ' age: ' + str(Student.__age) + ' gender: ' + str(Student.__gender))
        #Student.print_Student_doc()
        self.print_Student_doc()

    @classmethod
    def print_Student_doc(cls):
        print('name: ' + str(cls.__name) + ' age: ' + str(cls.__age) + ' gender: ' + str(cls.__gender))


student = Student('Justin', 34, '男')
student.print_student_doc()
student.print_Student_doc()    #正确，对象可以访问类函数
print(Student.__dict__)
Student.print_Student_doc()
#Student.print_student_doc() #错误，类函数不能访问对象函数