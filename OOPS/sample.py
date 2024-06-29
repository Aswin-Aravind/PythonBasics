# class Student:
#     def __init__(self,name,age,qualification):
#         self.name=name
#         self.age=age
#         self.qualification=qualification

#     def Display(self):
#         print("Name is",self.name,", he is",self.age,"and he completed,",self.qualification)

#     def Display_name(self):
#         print(self.name)

#     def Display_qualification(self):
#         print(self.qualification)

# obj1=Student(name="jithin",age="25",qualification="btech")
# obj1.Display()
# obj1.Display_name()
# obj1.Display_qualification()


# without class, just function

# def person(n,a,q):
#     return n
# k=person("Aswin",23,"Bsc CA")
# print(k)


# class Vehicle:
#     def __init__(self,type,yop,company,fuel):
#         self.type=type
#         self.yop=yop
#         self.company=company
#         self.fuel=fuel

#     def Display(self):
#         print("Type is",self.type,", manufactured on",self.yop,"by",self.company,"and it running on",self.fuel)
    
#     def Display_a(self):
#         print(self.company,self.type)

#     def Display_b(self):
#         print(self.fuel,self.company)
# obj1=Vehicle(type="4WD",yop=2022,company="Ford",fuel="Diesel")
# obj1.Display()
# obj1.Display_a()
# obj1.Display_b()


# create rectangleclass

# class Rectangle: 
#     def __init__(self,lenght,width):
#         self.lenght=lenght
#         self.width=width

#     def Display_a(self):
#         print("Area is",self.lenght*self.width)

#     def Display_p(self):
#         print("Perimeter is,",2*(self.lenght+self.width))

# k=Rectangle(lenght=6,width=5)
# k.Display_a()
# k.Display_p()


# class BOOK

# class Book:
#     def __init__(self,title,author,py):
#         self.title=title
#         self.author=author
#         self.py=py
    
#     def Display(self):
#         print("The book is",self.title,"written by",self.author,"and it was published on",self.py)

# k=Book(title="Les Miserables",author="Victor Hyugo",py=1862)
# k.Display()


# class Bank account

# class Bankaccount:
#     def __init__(self,accno,balance):
#         self.accno=accno
#         self.balance=balance

        
#     def Deposit(self,amount):
#         self.balance=self.balance+amount
#         return self.balance
    
#     def Withdraw(self,amount):
#         if amount>self.balance:
#             return False
#         else:
#             self.balance==amount
#             return self.balance


# k=Bankaccount(accno=2344,balance=3000)
# print(k.Deposit(amount=3000))
# print(k.Withdraw(amount=7000))



# inheritance


# class Parent:
#     def __init__(self,bike,car):
#         self.bike=bike
#         self.car=car
#     def display(self):
#         return self.car
# class Child(Parent):

#  obj1=Parent(bike="passion",car="I10")
#  print(obj1.display())

# obj2=Child(bike="passion",car="I10")
# print(obj2.display())



# class Parent:                #Single Inheritance
#     def __init__(self):
#         self.car="i10"
#         self.bike="rtr"
#     def display(self):
#         return self.bike
    
# class Child(Parent):
#      pass
# obj1=Child()
# print(obj1.display())


# Multilevel inheritance


# class Parent:
#     def info(self):
#         return "used for sample."
# class Car(Parent):
#     pass
# class Bike(Car):
#     pass

# obj1=Bike()
# print(obj1.info())


# Multiple Inheritance


# class Vehicle:
#     def display(self):
#         return "4 wheeler"

# class Car:
#     def info(self):
#         return "Nexon"
    
# class Nexon(Vehicle,Car):
#     pass
# obj1=Nexon()
# print(obj1.display())
# print(obj1.info ())



# class Vehicle:
#     def car(self):
#         return "Nexon"
#     def bike(self):
#         return "Apache"

# class Vehicle_child(Vehicle):
#     def bus(self):
#         return "Tata"
# obj=Vehicle_child()
# print(obj.bike())
# print(obj.car())
# print(obj.bus())
# obj1=Vehicle()
# print(obj1.car())
# print(obj1.bike())
# print(obj1.bus())


# class Register:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.course="python"

#     def display(self):
#         if self.age>18:
#             return self.name,self.course,self.age
#         else:
#             return "under age"
# obj=Register(name="Arya",age=17)
# print(obj.display())


# Calculator program

# class Calculator:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
    
#     def display(self):
#         self.n1=int(input("Enter first number:"))
#         self.n2=int(input("Enter second number:"))
    
#     def add(self):
#         return self.n1+self.n2
    
#     def sub(self):
#         return self.n1-self.n2
#     def mul(self):
#         return self.n1*self.n2
#     def div(self):
#         return self.n1//self.n2

# k=Calculator(n1=8,n2=4)
# print(k.add())
# print(k.sub())
# print(k.mul())
# print(k.div())


# class Details:
#     def __init__(self,name,age,profession,gender):
#         self.name=name
#         self.age=age
#         self.profession=profession
#         self.gender=gender
    
#     def m1(self):
#         print("Name is",self.name,", he is",self.age)

#     def m2(self):
#         print("Name is",self.name,", his job is",self.profession)

#     def m3(self):
#         print("His profession is",self.profession,"and he is a",self.gender)

#     def m4(self):
#         print("Name is",self.name,", he is",self.age,"he is working as",self.profession,"and he is a",self.gender)

# k=Details(name="Balu",age=24,profession="electrical engineer",gender="male")
# k.m1()
# k.m2()
# k.m3()
# k.m4()

    

# class Student:
#     name=str
#     age=int
#     marks=float
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def Display(self):
#         print("Name:",self.name,"\tAge:",self.age,"\tMarks:",self.marks)

#     def Calculate(self):
#         if self.marks>=90:
#             print("Grade:A")
#         elif self.marks>=80:
#             print("Grade:B")
#         elif self.marks>=70:
#             print("Grade:C")
#         elif self.marks>=60:
#             print("Grade:D")
#         else:
#             print("Grade:F")

# k=Student(name="Abhay",age=21,marks=73.5).Calculate()
# k1=Student(name="Bibin",age=25,marks=86.1).Calculate()
# k2=Student(name="Arnold",age=25,marks=68.1).Calculate()


# for i in k,k1,k2:
 
#  k.Display()
#  break
# k1.Display(),k1.Calculate()
# k2.Display(),k2.Calculate()



# Consider the Python class users provided below. 
# The class is designed to manage user data, 
# including operations like retrieving all user data,
# getting information about a specific user by ID,
# adding a new user, deleting a user by ID,
#  and updating user information.


# class Users:
#     data=[
#         {"id":1,"username":"anu","email":"anu@gmail.com","password":"password@123"},
#         {"id":2,"username":"achu","email":"achu@gmail.com","password":"password@123"},
#         {"id":3,"username":"ammu","email":"ammu@gmail.com","password":"password@123"},
#         {"id":4,"username":"manu","email":"manu@gmail.com","password":"password@123"},
#         {"id":5,"username":"Thanu","email":"thanu@gmail.com","password":"password@123"},
#         {"id":6,"username":"ann","email":"ann@gmail.com","password":"password@123"},
#     ]

#     def get_all_data(self):
#       return self.data
    
#     def get_one_data(self,id):
#        for i in self.data:
#           if i["id"]==id:
#              return i
    
# k=Users()
# # print(k.get_all_data())
# print(k.get_one_data(1))
