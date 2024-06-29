print("1.Square","\t","2.Triangle")
n = int(input("Enter your choice:"))
if n == 1:
    print("You chose Square")
    s = int(input("Enter the value of first side:"))
    area1 = (s**2)
    print("Area is",area1)
elif n == 2:
    print("You chose Triangle")
    base = int(input("Enter the value of base:"))
    height = int(input("Enter the value of height:"))
    area2 = (base*height)/2
    print("Area is",area2)
else:
    print("Error.")