# n = int(input("Enter the range:"))
# if n>0:
#     for i in range(2,n+1,2):
#         print(i)
# elif n == 0:
#     print("0")
# else:
#     print("Negative value.")

n = int(input("Enter first number"))
m = int(input("Enter second number"))
p = int(input("Enter third number"))

if n>m and n>p:
    print(n,"is greater.")
elif m>n and m>p:
    print(m,"is greater")
else:
    print(p,"is greater.")
    