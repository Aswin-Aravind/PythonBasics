expenses=[1000,2500,3500,12500,9876,6543]
# # print(max(expenses))
# # print(min(expenses))
expenses.extend([1234,456,6542])
# # print(expenses)
expenses.insert(3,8767)
# # print(expenses)
# # expenses.pop(4)  #or del expenses[4]
print(expenses)

n=[]
for i in expenses:
    if i>3000 and i<10000:
        print(i)
        n.append(i)
print(n)
expenses.clear()
expenses.append(n)
print(expenses)

#       
# expenses.append(i)
# print(expenses)
    
    
       
      
