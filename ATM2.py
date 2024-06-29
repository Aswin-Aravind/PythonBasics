import random
password = random.randint(1000,1005)
balance = random.randint(0,10000)
count=0
c = int(input("Enter your choice. 1.Withdraw  2.Balance  3.Exit"))
if c==1:
    for i in range(3):
        p=int(input("Enter the pin:"))
        if p==password:
            n=int(input("Enter the amount:"))
            if n<balance:
                print("Amount is debited.")
                print("Account balance is,",balance-n)
            else:
                print("Insufficient balance.")
        else:
            count=count+1
            if count==3:
                print("Card is blocked.")
            else:
                print("Try again.")
elif c==2:
    print("A/c balance is,",balance)
else:
    print("You are exiting.")
    exit()
