n = int(input("Enter your mark."))
if n>=0 and n<=100:
    if n>=90 and n<=100:
        print("A grade.")
    elif n<90 and n>=80:
        print("B grade")
    elif n<80 and n>=70:
        print("C grade.")
    elif n<70 and n>=60:
        print("D grade.")
    elif n<60:
        print("Failed.")
else:
    print("Invalid input.")    

