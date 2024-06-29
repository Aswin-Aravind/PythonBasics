n = int(input("Enter the starting year:"))
m = int(input("Enter the current year"))
for i in range(n,m+1):
  if i%4 == 0 and i%100 == 0 and i%400 == 0:
    print(i,"is a leap year and a century.")
  elif i%4 == 0 and i%100 == 0:
     print(i,"is not a leap year but century.")
  elif i%4 == 0:
     print(i,"is a leap year.") 

print("thank you")