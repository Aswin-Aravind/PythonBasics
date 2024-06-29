#1.  Write a Python function to find the maximum of three numbers.

# def Find(*args):
#     return max(args)
# obj=Find(2,5,9)
# print(obj)


#2. Write a Python function to sum all the numbers in a list.

# def Sum(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#     print(sum,"is the sum of the list.")
# lst=[8,2,3,0,7]
# k=Sum(lst)


#3. Write a Python function to multiply all the numbers in a list.
	# Sample List : (8, 2, 3, -1, 7)
	# Expected Output : -336

# def Product(l):
#     product=1
#     for i in l:
#         product=product*i
#     print(product)
# lst=[8,2,3,-1,7]
# k=Product(lst)


#4. Write a Python program to reverse a string.

# s="lumos maxima"
# print(s[::-1])


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# def Fact(x):
#     factorial=1
#     for i in range(1,x+1):
#         factorial=factorial*i
#     return factorial
# k=Fact(10)
# print(k)

# 0r

# import math
# def Fact(n):
#     return math.factorial(n)
# k=Fact(10)
# print(k)


#6. Write a Python function to check whether a number falls within a given range.

# def Falls(n):
#     for n in range(4,16):
#         if n in range(4,16):
#             print("Number falls in the range.")
#             break
#         else:
#             print("Number does not falls in the range.")
#             break
# k=Falls(10)


#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	# Sample String : 'The quick Brow Fox'
	# Expected Output :
	# No. of Upper case characters : 3
	# No. of Lower case Characters : 12

# def Cases(n):
#     count1=0
#     count2=0
#     for char in n:
#         if char.isupper():
#             count1+=1
#         elif char.islower():
#             count2+=1
#     print("No. of Upper case characters :",count1)
#     print("No. of Lower case Characters :",count2)
# k=Cases("The quick Brow Fox")


#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# def Distinct(l):
#     m=[]
#     for i in l:
#         if l.count(i)==1:
#             m.append(i)
#     return m
# lst=[1,1,5,6,7,7,16]
# obj=Distinct(lst)
# print(obj)


#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# def Prime(n):
#     count=0
#     for i in range(2,n):
#         if n%i==0:
#             count+=1
#             print("It is not a prime number.")
#             break
#     if count==0:
#             print("It is a prime number.")
# k=Prime(2)


# 10. Write a Python function that checks whether a passed string is a palindrome or not.

# def Palindrome(n):
#     s=n[::-1]
#     if s!=n:
#         print("String is not a palindrome.")
#     else:
#         print("String is a palindrome.")
# k=Palindrome("NIBIN")


# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print("Area of circle is:",3.14*self.radius**2)
#     def circumference(self):
#         print("Circumference is:",2*3.14*self.radius)
    
# k=Circle(radius=4)
# k.area()
# k.circumference()


# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.


# class Person():
#     def __init__(self,name,country,dob,current_year=2024):
#         self.name=name
#         self.country=country
#         self.dob=dob
#         self.current_year= 
#     def age(self):
#         print("age of person is",self.current_year-self.dob)
        
# k=Person(name="Arnold",country="UAE",dob=)


# 4. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price


# class Shoppping:
#     def __init__(self):
#         self.items={}
        
#     def add_item(self,product,price):
#         self.items[product]=price
#         return print(self.items)
#     def remove_item(self,product):
#         del self.items[product]
#         return print(self.items)
#     def total(self):
#         x=sum(self.items.values())
#         return print(x)
    
# k=Shoppping()
# k.add_item(product="p1",price=100)
# k.add_item(product="p2",price=300)
# k.remove_item(product="p1")
# k.total()

            
            


class Mobiles:

    data=[
        {"id":100,"name":"galaxy","price":35000},
        {"id":101,"name":"Mi 11","price":45000},
        {"id":102,"name":"Iphone 11","price":130000},
        {"id":103,"name":"s23","price":100000},
        {"id":104,"name":"neo","price":39000},
    ]

    def display(self):
        return self.data
    
    def specific_mobile(self,id):
        for i in self.data:
            id=i.get("id")
            if id==id:
                return i
            else:
                return "error"
            
    def update_mobile(self,id):

        for i in self.data:
            id=i.get("id")
            if id==id:

                i.update(new)
                    
        
    

obj = Mobiles()
# print(obj.display())
# print(obj.specific_mobile(100))

print(obj.update_mobile(103))

