compnum = 50
m = int(input("Guess the number"))
count = 1
while m!=compnum:
    
    if m<compnum:
        print("too low")
    elif m>compnum:
        print("too high")
    m = int(input("Guess the number"))
    count = count+1
print("Well done you took,",count,"attempts.")
print("You are correct.")
