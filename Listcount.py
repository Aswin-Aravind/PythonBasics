
number=[-2,3,-14,5,-7,-9,10,-12,11]
count=0
flag=0
for i in number:
    if i>0:
        count+=1
    else:
        flag+=1
print("Positive integers are:",count)
print("Negative integers are:",flag)