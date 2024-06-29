nums=[]
for i in range(3):
    nums.append(input("Add number:"))
print(nums)
m=input("Do you want to keep the last number?y/n:")
if m=="y":
        print("It is saved.")
        print(nums)
else:
        nums.pop()
        print(nums)
    