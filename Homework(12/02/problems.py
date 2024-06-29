# 1. Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.


# class Students:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

#     def display(self):
#         print(f"Name:{self.name}\nAge:{self.age}\nGrade:{self.grade}")

# k=Students("Aswin",23,"A")
# k.display()


# 2. Write a program to create a child class Teacher that will inherit the properties of Parent class Staff

# class Staff:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender

# class Teachers(Staff):
#     def __init__(self, name, gender,age,subject):
#         self.age=age
#         self.subject=subject
#         super().__init__(name, gender)

#     def display(self):
#         print(f"Name:{self.name}\nGender:{self.gender}\nAge:{self.age}\nSubject:{self.subject}")

# k=Teachers("Arnold","Male",24,"History")
# k.display()


# 3.Write a Python class Square, and define two methods that return the square area and perimeter.


# class Square:
#     def perimeter(self,length):
#         self.length=length
#         return "Perimeter is:",4*self.length
    
#     def area(self,length):
#         self.length=length
#         return "Area is:",self.length*self.length
    
# k=Square()
# print(k.perimeter(6))
# print(k.area(6))   


# 4.define an account cclass with attributes ac no,ac name,balance.

# class Account:
#     def __init__(self,ac_no,ac_name,balance):
#         self.ac_no=ac_no
#         self.ac_name=ac_name
#         self.balance=balance

#     def display(self):
#         print(f"Account number:{self.ac_no}\nAccount name:{self.ac_name}\nBalance:{self.balance}")

# k=Account(12345,"Joint Account",75000)
# k.display()


class Course:
    course={}

    def 