# 035
# name = input("Enter you name:")
# for i in range(1,4):
#     print(name)


#036
# name = input("Enter your name:")
# n = int(input("Enter the range of number which you want to repeat your name:"))
# for i in range(1,n+1):
#     print(name)


# 037 
# name = input("Enter your name:")
# for i in name:
#     print(i)


# 038
# name = input("Enter your name:")
# n = int(input("How many times you want repeat?"))
# for i in range(1,n+1):
#   for i in name:
#     print(i)


# 039
# x = 0
# n = int(input("Enter a number between 1 and 12:"))
# if n<1 or n>12:
#     print("Error.")
# else:
#     for i in range(1,11):
#         print(i,"*",n,"=",i*n)


# 040
# n = int(input("Enter a number below 50:"))
# if n>=50:
#     print("ERROR.")
# else:
#     for i in range(50,n-1,-1):
#         print(i)


# 041
# name = input("Enter your name:")
# n = int(input("How many times you want to repeat?"))
# if n>=10:
#     print("Too high.")
# else:
#     for i in range(1,n+1):
#         print(name)


# 042
# total = 0
# for i in range(1,6):
#     n = int(input("Enter the number:"))
#     m = input("Do you want to add this number? Yes or No :")
#     if m=="yes":
#       total = total+n
#     else:
#       print("not added")
# print(total)


# 043
# x = input("Which direction you want to count. Up or Down?")
# if x=="up":
#     n = int(input("Enter the range:"))
#     for i in range(1,n+1):
#         print(i)
# elif x=="down":
#     m = int(input("Enter a value below 20:"))
#     if m<20:
#         for i in range(20,m-1,-1):
#             print(i)
#     else:
#         print("ERROR")
# else:
#     print("I don't understand.")


# 044
# n = int(input("How many people do you want to invite?"))
# if n<10:
#     for i in range(1,n+1):
#      m = input("Enter your name:")
#      print(m,"has been invited to the party.")
# else:
#    print("Too many people!")


# whatsapp h/w
import random
num = random.randint(0,21)
print(num)
if num==0:
   for i in range(1,11):
      sum = 10*(10+1)/2
print("Sum of 1 to 10 is",sum)
if num%2!=0:
    for i in range(1,num+1,2):
        print(i)
elif num%2==0:
    for i in range(1,13):
        print("Multiplication table for",i,"is:")
        for j in range(1,11):
         print(j,"*",i,"is =",i*j)

    # or sum = sum+1