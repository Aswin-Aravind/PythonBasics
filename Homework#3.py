# 012
# n = int(input("Enter first number:"))
# m = int(input("Enter second number:"))
# if n>m:
#     n,m = m,n
#     print(n,",",m)
# else:
#     print(n,",",m)


# 013
# n = int(input("Enter a number below 20:"))
# if n>=20 :
#     print("Too high.")
# else:
#     print("Thank you.")


# 014
# n = int(input("Enter a number between 10 and 20(10 & 20 inclusive):"))
# if n>=10 and n<=20:
#     print("Thank you.")
# else:
#     print("Incorrect answer.")


# 015
# color = input("Enter your favourite colour:")
# if color == "RED" or color == "red" or color == "Red":
#     print("I like red too.")
# else:
#     print("I don't like",color,", I prefer red.")


# 016

# n = input("Is it raining? Yes or No:").lower()
# if n=="yes":
#     m = input("Is it windy? Yes or No:").lower()
#     if m=="yes":
#         print("It is too windy for an umbrella.")
#     else:
#         print("Take an umbrella.")
# else:
#     print("Enjoy your day.")


# 017
# n = int(input("Enter your age:"))
# if n>=18:
#     print("You can vote.")
# elif n==17:
#     print("You can learn to drive.")
# elif n==16:
#     print("You can buy a lottery ticket.")
# elif n<16:
#     print("You can go Trick-or-Treating.")


# 018
# n = int(input("Enter a number:"))
# if n<10:
#     print("Too low.")
# elif n>=10 and n<=20:
#     print("Correct")
# else:
#     print("Too high.")


# 019
# n = int(input("Enter 1,2 or 3:"))
# if n==1:
#     print("Thank you")
# elif n==2:
#     print("Well done.")
# elif n==3:
#     print("Correct")
# else:
#     print("Error message.")


# 052
# import random
# num = random.randint(1,100)
# print(num)


# 053
# import random
# fruits = ("Passion Fruit","Grape","Mango","Orange","Apple")
# print(random.choice(fruits))


# 054
# import random
# result = ["h","t"]
# r = random.choice(result)
# n = input("Enter your choice; h or t:")
# if n==r:
#     print("You win.")
# else:
#     print("Bad luck.")
# print("Computer selected",r)


# 055
# import random
# num = random.randint(1,5)
# n=int(input("Guess the number:"))
# if n==num:
#     print("Well Done.")
# else:
#     if n>num:
#         print("Too high.")
#     elif n<num:
#         print("Too less.")
#     n=int(input("Guess the number once more:"))
#     if n==num:
#         print("Correct")
#     else:
#         print("You lose.")


# 056
# import random
# num = random.randint(1,10)
# n = int(input("Enter the number:"))
# while True:
#     if num==n:
#         print("Correct")
#         break
#     else:
#         n = int(input("Enter the number again:"))


# 057
# import random
# num = random.randint(1,10)
# n = int(input("Enter the number:"))
# while True:
#     if num==n:
#         print("Correct")
#         break
#     else:
#         if n>num:
#             print("Too high.")
#         elif n<num:
#             print("Too low.")
#         n = int(input("Enter the number again:"))


# 058
# import random
# score=0
# for i in range(5):
#    num1 = random.randint(0,100)
#    num2 = random.randint(0,100)
#    result = num1+num2
#    print(num1,"+",num2,"=")
#    answer = int(input("Answer is:")) 
#    if result==answer:
#            print("Correct.")
#            score = score+1
#    else:
#          print("Wrong.")
# print("You got",score,"out of 5.")


# 059
import random
color = ["Blue","Yellow","Green","Purple","Black"]
c = random.choice(color).lower()
n = input("Guess the colour?") 
while n!=c:
   print("You must be feeling",c.upper(),"right now.")
   n = input("Guess the colour?")
   if c==n:
    print("Well done.") #mission accomplished. :)





 

