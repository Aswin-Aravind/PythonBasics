# number=[5,4,7,4,4,9,3,1]
# m=int(input("Which number do you want to delete?"))
# for i in number:
#     if i==m:
#         number.remove(m)
# print(number)
#     # else:
#     #     print("Not in the list.")
#     #     break



number=[5,4,7,4,4,9,3,1]
print(number)
n=int(input("Enter the round:"))
for i in range(n):
  l= number.pop()
  number.insert(0,l)
  print(number)