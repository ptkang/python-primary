'''
@Author: your name
@Date: 2019-11-26 22:16:44
@LastEditTime: 2019-11-27 23:47:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\class\c1.py
'''
# 面向对象
# 写出有意义的面向对象的代码
# 类最基本的作用是封装代码（变量+函数）
# 类变量和对象变量
# self代表实例而非类
# 实例变量和实例方法是和实例对象相关联的
# 类包括特征和方法
class Student():
    sum = 0
    #name = '石敢当'
    #age = 21
    #gender = '女'
    def __init__(self, name, age1, gender):
        self.name = name
        self.age = age1
        self.gender = gender
        self.plus_sum() #self.__class__.sum += 1  # 或Student.sum += 1
        #print('name: ' + str(name) + ' age: ' + str(age) + ' gender: ' + str(gender))
        print('name: ' + str(self.name) + ' age: ' + str(self.age) + ' gender: ' + str(self.gender))
        print('id(name)=' + str(id(name)))
        print('id(self.name)=' + str(id(self.name)))
        print('id(age1)=' + str(id(age1)))
        print('self.age is age1', self.age is age1)
        print('self.age == age1', self.age == age1)
        print('type(self.age)', type(self.age))
        print('type(age1)', type(age1))
        #print('object.__eq__(self, self.age, age1)=', object.__eq__(self, self.age, age1))
        print('id(self.age)=' + str(id(self.age)))
        print(self.__dict__)
    def print_student_doc(self):
        print('name: ' + str(self.name) + ' age: ' + str(self.age) + ' gender: ' + str(self.gender))
        print(self.__dict__)
    
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('cls.sum=', cls.sum)

    @staticmethod
    def add(x, y):
        print('x + y = ', x + y)
        

student1 = Student('Justin', 34, '男')
student1.print_student_doc()
print('sum=' + str(Student.sum))
student2 = Student('Peter', 32, '女')
student2.print_student_doc()
print('sum=' + str(Student.sum))
print(student1.__dict__)
print(Student.__dict__)
#Student.plus_sum()
Student.add(1, 2)
student1.add(3, 4)

#print('name: ' + str(student.name) + ' age: ' + str(student.age) + ' gender: ' + str(student.gender))
#print('name: ' + str(Student.name) + ' age: ' + str(Student.age) + ' gender: ' + str(Student.gender))