class Person:
    age = 32
    print(age)
p1 =Person()
print(p1.age)
p2 =Person()
print(p2.age)
p3 =Person()
print(p3.age)




class Student():
    Grade = 'A'
    print(Grade)

Student1 =Student()

student2 =Student()
print(Student1.Grade)

Student3 =Student()
print(Student1.Grade)

class employees:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
Employee1 = employees('Sophia', 45,'kahawa')
# Employee2 =employees('Joann', 18,)
# Employee3 =employees('Sophia', 45)
print(Employee1)
# print(Employee2)
# print(Employee3)


# class University():
#     def __init__(self,name,location):
#         self.name = name
#         self.location = location
# university1 =University('JKUAT', 'Nairobi')
# university2 =University('UON', 'Nairobi')
# print(university1)
# print(university2)

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
         print('My name is',self.name)
s1 = Student('John', 22, 344)
# s2 = Student('David', 32, 364)
print(s1.display())
# print(s2.display())

# class Parents():
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


