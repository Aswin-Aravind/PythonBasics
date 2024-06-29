num = input("Enter the choice: u/d?")
if num=="u":
    n=int(input("Enter the range:"))
    for i in range(1,n+1):
     print(i)
elif num=="d":
    k = int(input("Enter the range less than 20:"))
    for i in range(20,k,-1):
          print(i)
else:
   print("Get out.")
       