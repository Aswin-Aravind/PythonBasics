import random
num = random.randint(1,5)
n = int(input("Guess the number:"))
if n==num:
    print("Well Done.")
elif n>num:
    print("Too high.")
    n=int(input("Guess again"))
    if n==num:
        print("Correct")
    else:
        print("You lose.")
else:
    print("Too low.")
    n=int(input("Guess again"))
    if n==num:
        print("Correct")
    else:
        print("You lose.")