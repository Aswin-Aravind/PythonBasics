# # n=0
# # m = int(input("Enter the value:"))
# # while m == 0:
# #     =m+n

# # n = int(input("Enter the value"))
# # if n<5:
# #     for i in range(1,11):
# #         print(n*i)
# # else:
# #     print("Error.")


# n = 1
# m = int(input("Enter the range:"))
# while n<=m:
#        print(n)
#        n = n+1

# n = 1
# m = int(input("Enter the range:"))
# while(n<=m):
#     if n%2==0:
#         print(n)
#         n = n+1
#     else:
#         n=n+1          OR

# n = 1
# m = int(input("Enter the range:"))
# while(n<=m):
#     if n%2==0:
#         print(n)
#     n = n+1            OR


n = int(input("Enter a value between 10 and 20:"))
while n<10 or n>20:
 if n<10:
    print("Too low, please try again.")
 elif n>20:
    print("Too high, please try again.")
 n = int(input("Try again:"))

print("success")