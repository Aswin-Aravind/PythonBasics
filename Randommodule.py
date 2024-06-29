import random
num = random.randint(1,10)

for i in range(10):
    n = int(input("Enter the number:"))
    if i== num:
        print("Correct")
        break
    else:
        print("Try again.")
print("Thank you")