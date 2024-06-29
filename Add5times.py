total = 0
for i in range(1,6):
    n = int(input("Enter the number:"))
    m = input("Do you want to add this number?")
    if m=="yes":
        total = total+n
    else:
        print("Not added")
print(total)