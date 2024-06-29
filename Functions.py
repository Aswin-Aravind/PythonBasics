# function calling,fun open, fun evaluation,return




#specific task
#reduce code repetiotion
# function calling

# def Greet(name):
#     return "hello, "+ name
# obj=Greet("aswin")
# print(obj)


# def Length(name):
#     return len(name)
# name="aswin"
# obj=Length(name)
# print("Length of the name is, "+obj)


# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def division(a,b):
#     return a/b
# n=int(input("Enter your choice: \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division"))
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# if n==1:
#     print(n1,"+",n2,"=",add(n1,n2))
# elif n==2:
#     print(n1,"-",n2,"=",sub(n1,n2))
# elif n==3:
#     print(multiply(n1,n2))
# elif n==4:
#     print(division(n1,n2))
# print()

# SWAP

# def sub(a,b):
#     if a<b:
#         a,b=b,a
#     # else:
#     #     print("ALlergic to -ve values.")
#     return a-b
# result=sub(1,8)
# print(result)  


# ODD OR EVEN

# def find(n):
#     if n%2==0:
#         x=n,"is even."
#     else:
#         x=n,"is odd."
#     return x
# obj=find(3)
# print(obj)


# #TELL IF NUMBER IS BTW 1 and 90
# n=int(input("Enter a number:"))
# def find(n):
#     if n>1 and n<90:
#         result="It is btw 1 and 90."
#     else:
#         result="It is not btw 1 and 90."
#     return result
# obj=find(n)
# print(obj)


# OR
















# Default Arguments


# def add(a,b=10):
#     return a+b
# print(add(10))


# def add(*args):
#     return sum(*args)
# result=add([1,2,3,4])
# print(result)  


# from the list find the unique number(23/01/2024)
# l=[1,2,3,4,1,3,4,1,3]
# for i in l:
#     if l.count(i)==1:
#      print(i,"is the unique one.")


# same prg with function****
# def unique_value(l):
#     new=[]
#     for i in l:
#         if l.count(i)==1:
#             new.append(i)
#             print(i,"is the unique value.")
#     return new
# lst=[1,2,3,4,1,3,4,1,3]
# result=unique_value(lst)
# print(result,"is the unique value.")

# def find_unique_value(lst):
#     unique_values = []

#     for i in lst:
#         if lst.count(i) == 1:
#             unique_values.append(i)
#             print(i, "is a unique value.")

#     return unique_values

# # Example
# l = [1, 2, 3, 4, 1, 3, 4, 1, 3]
# result = find_unique_value(l)
# print("Unique values:", result)


# OR
# l=[1,2,3,4,1,3,4,1,3]
# m=[]
# for i in l:
#     if i in m:
                    #    do again with function
#     else:
        
#         m.append(i)


# find reverse of the string
# name=" aswiN aravinD"
# print(name[::-1])

# or

# name= "aswiN aravinD"
# rev_word=" "
# for i in name:
#     rev_word= i +rev_word
# print(rev_word)


# print reverse of the given list
# l=["hello","cat","malayalam"]
# m=[]
# for i in l:
#     i=i[::-1]
#     m.append(i)
# print(m)


# reverse in function

# def rev_word(word):
#     return word[::-1]
# k=rev_word("aswiN")
# print(k)


# reverse list in function

# def rev_word(l):
#     return  
#     for i in l:      #do it again
    
# l=["hello"]
    



# kore values kodukum, even numbers print cheyyanam

# def v(*args):
#     l=[]
#     for i in args:
#         if i%2==0:
#             l.append(i)
#     return l
# k=v(1,4,2,3,5,8,11,7)
# print(k)



# Homeworks of 30/1/2024


# def values(l1,l2):
#     unique_values=set(l1)^set(l2)
#     return list(unique_values)
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]

# k=values(l1,l2)
# print(k)






# def multiples(n):
#     m=[]
#     for i in range(1,n):
#         if n%i==0:
#             m.append(i)
#     print(m)
# n=int(input("Enter a number:"))
# k=multiples(n)


# n=int(input("Enter a number:"))
# for i in range(1,n):
#     if n%i==0:
#         print(i)