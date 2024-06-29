# 105

# file=open("Numbers.txt","w")
# file.write("9,7,4,7,4,7")
# file.close()
# file=open("Numbers.txt")
# print(file.read())


# 106 & 107

# file=open("Names.txt","w")
# file.write("Aravi \nSushama \nArya \nVaishnavi \nAswin")
# file.close()
# file=open("Names.txt")
# print(file.read())


# 108

# file=open("Names.txt","a")
# name=input("Enter new name:")
# file.write("\n"+name)
# file.close()
# file=open("Names.txt")
# print(file.read())


# 109

# query=int(input("1) Create a new file. \n2) Display the file. \n3) Add a new item to the file. \nMake a selection 1, 2 or 3:"))
# if query==1:
#     file=open("Subject.txt","w")
#     file.write(input("Enter a school subject:"))
#     file.close()
# elif query==2:
#     file=open("Subject.txt")
#     print(file.read())
# elif query==3:
#     file=open("Subject.txt","a")
#     name=input("Enter a new subject:")
#     file.write(", "+name)
#     file.close()
#     file=open("Subject.txt")
#     print(file.read())
# else:
#     print("Wrong option.")


# 110
# import os
# file=open("Names.txt")
# s=file.read()
# print(s)
# name=input("Enter a name in the list:")
# if name in s:
#     del name
# file2=open("Names2.txt","a")
# file2.write(s)
# file.close()





# Python to count total number of upper case and lower case character in a file
# file=open("Random.txt","w")
# file.write("SectuMsemPRA")
# file.close()
# file=open("Random.txt")
# s=file.read()
# print(s)
# upper_case= [i for i in s if i==i.upper()]
# lower_case= [i for i in s if i==i.lower()]
# print("There are",len(upper_case),"upper case in the file.")
# print("There are",len(lower_case),"lower case in the file.")

# Or

# file=open("Random.txt")
# s=file.read()
# upper_case=[]
# lower_case=[]
# for i in s:
#     if i==i.upper():
#         upper_case.append(i)
#     elif i==i.lower():
#         lower_case.append(i)
# print("There are",len(upper_case),"upper cases.")
# print("There are",len(lower_case),"lower cases.")

# Or

# file=open("Random.txt")
# count1=0
# count2=0
# s=file.read()
# for i in s:
#     if i==i.upper():
#         count1+=1
#     else:
#         count2+=1
# print(count1,"upper cases.")
# print(count2,"lower cases.")
