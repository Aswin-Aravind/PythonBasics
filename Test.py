# n = input("Enter your first name:")
# if len(n)<5:
#     m= input("Enter the second name:")
#     x = n+m
#     print(x.upper())
# elif len(n)>=5:
#     print(n.lower())

# n = int(input("Enter your choice: 1.Square2.Triangle"))
# if n==1:
#     s = int(input("Enter the length of side:"))
#     a = s**2
#     print("Area of square is",a)
# elif n==2:
#     b = int(input("Enter the base length:"))

#     h = int(input("Enter the height length:"))
#     a = b*h//2
#     print("Area of triangle is",a)
# else:
#     print("Get out!")


# n = int(input("Enter a number btw 10 and 20:"))
# if n<10:
#     print("Too low!")
# elif n>10 and n<20:
#     print("Correct.")
# elif n>20:
#     print("Too high!")
# print("Thank you.")

# h = float(input("Enter your height in metres:"))
# w = int(input("Enter your weight in kilogram:"))
# bmi = w//h**2
# print(bmi)
# if bmi<19:
#     print("Below normal.")
# elif bmi>=19 and bmi<25:
#     print("normal")
# else:
#     print("Overweight")

# n = int(input("Enter a range(Integer value):"))
# if n<1:
#     print("Enter positive integer value!")
# if n%2==0:
#     sum = n*(n+1)
#     print(sum)
# elif n%2!=0:
#     sum = n**2
#     print(sum)

n = int(input("Enter a number:"))
sum=0
if n<1:
    print("Enter a positive Integer.")
elif n%2==0:
     for i in range(2,n+1,2):
        sum = sum+i
     print(sum)
elif n%2!=0:
       for i in range(1,n+1,2):
          sum = sum+i
       print(sum)
print("Thank you.")