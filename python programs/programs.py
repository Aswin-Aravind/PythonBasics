                       # -----------------------------PYTHON PROGRAMS---------------------#

# 1. Python Program to Find LCM

# def get_lcm(x,y):
#     if x>y:
#         greater=x
#     else:
#         greater=y

#     while True:
#         if greater%x==0 and greater%y==0:
#             lcm=greater
#             break
#         greater+=1
#     return lcm

# num1=12
# num2=18
# print("Lcm is:",get_lcm(num1,num2))


# 2. Python Program to Find HCF

# def get_hcf(x,y):
#     while y:
#         x,y=y,x%y
#     return x   
# k=get_hcf(12,30)
# print("The hcf is",k)


# 3. Python Program to Make a Simple Calculator

# def Calculator(num1,num2):
#     n=int(input("Enter the option;\t1.Addition\t2.Subtraction\t3.Multiplication\t4.Division: "))
#     if n==1:
#         return num1+num2
#     elif n==2:
#         return num1-num2
#     elif n==3:
#         return num1*num2
#     else:
#         return num1/num2
    
# n1=int(input("Enter the first number:"))
# n2=int(input("Enter the second number:"))
# print(Calculator(n1,n2))


# 4. Python Program to Find Factorial of Number Using Recursion

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num = int(input("Enter the number:"))

# if num<0:
#     print("There are no factorials for numbers below 0.")

# elif num==0:
#     print("Factorial of 0 is 1.")

# else:
#     print("The factorial is:",factorial(num))


# 5. Python program to check if the given number is a Disarium Number

# n=int(input("Enter the number:"))
# x=str(n)
# sum=0
# for i,j in enumerate(x):
#    sum+=int(j)**(int(i)+1)
# # print(sum)
# if sum==n:
#     print(f"{n} is a Disarium number.")
# else:
#     print(f"{n} is not a Disarium number.")


# 6. Python program to determine whether the given number is a Harshad Number.

# n=int(input("Enter the number:"))
# l=[]
# for i in str(n):
#     c=0
#     l.append(i)
#     for i in l:
#         x=int(i)
#         c+=x
# if n%c==0:
#         print("It is a Harshad number.")
# else:
#         print("It is not a Harshad number.")


# 7. Python program to check the number of digits present in a integer

# n=int(input("Enter the number:"))
# count=0
# for i in str(n):
#     count+=1
# print(f"{count} digits are there.")


# 8.How to count the number of upper and lowercase letters in a string

# n=input("Enter the word:")
# c1=0
# c2=0
# for char in n:
#     if char.isupper():
#         c1+=1
#     elif char.islower():
#         c2+=1
# print("There are",c1,"upper cases.")
# print("There are",c2,"lower cases.")


# 9. Write a program to count words in string

# n="Joins the Juggernaut"
# x= n.split()
# print(len(x))


# 10. Write the program to find the lists consist of at least one common element.
# lst=[]
# def common_element(l1,l2):
#     for i in l1:
#         if i in l2:
#             lst.append(i)
#     print(f"Common elements are: {lst}")
# l1=[2,3,6,7,4,9]
# l2=[1,2,7,5,8,3]
# common_element(l1,l2)
    

# 11. Python program to print the duplicate elements of an array
# lst=[]
# def duplicate(l):
#     print("Duplicate elements:")
#     for i in l:
#          if i in lst:
#           print(i)
#          else:
#             lst.append(i)
    
# l=[1,1,6,4,8,8]
# duplicate(l)


# 12. Python program to print the elements of an array present on even position.

# def even_position(l):
#     print("Even position elements are:")
#     for i,j in enumerate(l):
#         if i%2==0:
#             print(j)
# l=[1,2,3,4,5,6,7,8]
# even_position(l)


# 13. Python program to print the elements of an array present on odd position.

# def odd_position(l):
#     print("Odd position elements are:")
#     for i,j in enumerate(l):
#         if i%2!=0:
#             print(j)
# l=[1,2,3,4,5,6,7,8]
# odd_position(l)


# 14. Python program to print the largest element in an array.

# def largest(l):
#     return max(l)
# l=[4,5,23,5,78,56]
# print(largest(l))


# 15. Python program to print the smallest element in an array.

# def smallest(l):
#     return min(l)
# l=[23,5,78,56,-1,4]
# print(smallest(l))


# 16. Python program to print the number of elements present in an array.

# l=[1,5,4,5,7,3,3,6,8,8]
# print(len(l))


# 17. Python program to print the sum of all elements in an array

# l=[2,45,45,8]
# print(sum(l))


# 18. Python Program to Find Armstrong Number in an Interval.

# num1=int(input("Enter first limit:"))
# num2=int(input("Enter second limit:"))
# for i in range(num1,num2+1):  
#  x=len(str(i))
#  sum=0
#  flag=i
#  while flag>0:
#    n=flag%10
#    sum+=n**x
#    flag//=10
#  if i==sum:
#    print(i)


# 19. Program to Check Armstrong Numbers in Python.

# def armstrong(n):
#     x=len(str(n))
#     flag=n
#     sum=0
#     while flag>0:
#        num=flag%10
#        sum+=num**x
#        flag//=10
#     if n==sum:
#         print(n,"is an armstrong number.")
#     else:
#         print(n,"is not an armstrong number.")

# armstrong(n=int(input("Enter the number:")))


# 20. Write a Python program to reverse a string.

# n="Interesting facts"
# print(n[::-1])


# 21. Write a Python program to check if a list is empty or not.

# l=[]
# if l!=[]:
#   print("Not empty")
# else:
#   print("Empty.")

 
# 22. Write a Python program to multiply all the items in a list.

# def multiply_items(lst):
#     count=1
#     for i in lst:
#         count*=i
#     return count
# lst=[2,4,5,10]
# print(multiply_items(lst))


# 23. Write a Python program to clone or copy a list.

# def clone(lst):
#     l=[]
#     for i in lst:
#         if i not in l:
#             l.append(i)
#     return l
# lst=[7,4,2,6,4,1]
# print(clone(lst))

# 24. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# def remove_even_no(lst):
#     l=[]
#     for i in lst:
#         if i%2!=0:
#             l.append(i)
#     return l
# lst=[1,2,3,4,5,6,7,8]
# print(remove_even_no(lst))


# 25. Write a Python program to shuffle and print a specified list.

# from random import shuffle
# l=[4,6,3,8,3,0,2,45]
# shuffle(l)
# print(l)


# 26. Write a Python program to create a list with infinite elements.

# def infinite_elements(lst):
#     n=int(input("Enter the range:"))
#     while n!=0:
#         for i in range(1,n+1):
#             lst.append(i)
#         print(lst)
#         n=int(input("Enter the range:"))
# infinite_elements( lst=[])  


# 27. Write a Python program to check whether the n-th element exists in a given list.
# l=[5,7,8,5,3,5,7,6]
# print(l[-1])


# 28. Write a Python function to find the maximum of three numbers.

# def maximum(l):
#     return max(l)
# lst=[34,56,123]
# print(maximum(lst))


# 29. Write a Python function that accepts a string and counts the number of upper- and lower-case letters.

# def count_cases(s):
#     c1=0
#     c2=0
#     for i in s:
#         if i.isupper():
#             c1+=1
#         elif i.islower():
#             c2+=1
#         else:
#             pass
#     print(f"There are {c1} upper cases.\nThere are {c2} lower cases.")

# count_cases(s=input("Enter the string:")) 
    

#30. Write a Python program to reverse the order of the items in the array.

# names=["aswin","ajaz","bibin"]
# print(names[::-1])
# n1=[]
## for i in names:
# #    n1.append(i[::-1])
## print(n1) 