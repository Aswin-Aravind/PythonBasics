n = int(input("Enter the range:"))
for x in range(2,n+1):
 flag=0 
# x = int(input("Enter the number:"))
 for i in range(2,x):
      if x%i==0:
          print(x,"is not a prime number.")
          flag=flag+1
          break
 if flag==0:
     print(x,"is a prime number.")