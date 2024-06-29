import random
balance = random.randint(0,6500)
password = random.randint(1000,1001)
# count=0
for i in range(3):
 p = int(input("Enter the pin:"))
 if p==password:
     for i in range(3):
      c=int(input("Enter your choice: 1.Withdraw  2.Balance  3.Exit:"))
      if c==1:
         n=int(input("Enter the amount:"))
         if n<=balance:
             print("Amount is debited.")
             while True:
                 balance=balance-n
         else:
             print("Insufficient balance.")
      elif c==2:
         print("A/c balance is,",balance)
      else:
         print("You are exiting.")
         exit()
else:
            print("Card is blocked.")
    
print("Try Again.")
