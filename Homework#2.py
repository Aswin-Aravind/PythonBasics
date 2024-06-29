#045
# total = 0
# while total<=50:
#     n = int(input("Enter a  number:"))
#     total = total+n
#     print("The total is ",total)


# 046
# n = int(input("Enter a number:"))
# for i in range(n):
#     if n<=5:
#      n = int(input("Enter a number:"))
# print("The last number you entered was,",n)
 

# 047
# n = int(input("Enter 1st number:"))
# m = int(input("Enter 2nd number:"))
# x=m+n
# print("The result is,",x)
# while True:
#     a = input("Do you want to add this number? Yes or No").lower()
#     if a=="yes":
#         m = int(input("Enter the other number:"))
#         total = x+m
#     else:
#       print(total) 
#       break 

# 048
# n = input("Enter the name you wants to invite:")
# print(n,"has been invited to the party.")
# count=1
# while True:
#     m = input("Do you want to invite somebody else? Yes or No:").lower()
#     if m=="yes":
#         n = input("Enter the name you wants to invite:")
#         count = count+1
#     else:
#         print(count,"people were invited to the party.")


# 049
# compnum = 50
# n = int(input("Guess the number.:"))
# count = 1
# while compnum!=n:
#     if n<compnum:
#        print("Too low.")
#     elif n>compnum:
#         print("Too high.")
#     n = int(input("Guess the number.:"))
#     count = count+1
# print("Well done you took",count,"attempts.")


# 050
# n = int(input("Enter a number between 10 and 20:"))
# while True:
#     if n<10:
#      print("Too low.")
#      print("Try again")
#      n = int(input("Enter a number between 10 and 20:")) 
#     elif n>20:
#         print("Too high.")
#         print("Try again")
#         n = int(input("Enter a number between 10 and 20:"))
        
#     else:
#      print("Correct.")
#      print("Thank you")
#      break


 # 051


# num = 10
# while num>0:
#     print("There are",num,"green bottles hanging on the wall")
#     print(num,"green bottles hanging on the wall")
#     print("and if 1 green bottle should accidentally fall.")
#     num = num-1
#     m = int(input("How many green bottles will be hanging on the wall?"))
#     if m==num:
#         print("There will be",num,"green bottles hanging on the wall.")
#     else:
#         while m!=num:
#          m=input("No try again.")
#          break
# print("There are no more green bottles hanging on the wall.")



# 046 another solution
# n = int(input("Enter a number:"))
# while n<=5:
#     if n<=5:
#      n = int(input("Enter a number:"))
# print("The last number you entered was,",n)
