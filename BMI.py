weight = int(input("Enter the weight in kg:"))
height = float(input("Enter the height in m:"))

bmi = weight//height**2
print(bmi)

if bmi<19:
    print("Below normal!")
elif bmi>=19 and bmi<25:
    print("Normal.")
elif bmi>=25 and bmi<30:
    print("Overweight!")
else:
    print("Obese!")