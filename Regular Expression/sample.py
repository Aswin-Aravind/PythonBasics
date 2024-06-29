from re import *

string="qwertyuhefqhwqweryt"
pattern="u"

r=finditer(pattern,string)
for i in r:
    print(i.start())
    print(i.group())



# s=input("Enter the string:")
# n=input("Enter a pattern:")
# r=finditer(pattern=n,string=s)
# for i in r:
#     print(i.start(),i.group()) 


# s=input("enter the string:")
# n=input("Enter the pattern:")
# r=finditer(pattern=n,string=s)
# for i in r:
#     print(i.start(),i.group())



# string="fnfbkhdfjyerbssuasu"
# pattern=["su","kh"]
# for i in pattern:
#  r=finditer(i,string)
#  for n in r:
#   print(n.start(),n.group())



# s=input("Enter a string:")
# n=input("Enter a pattern(in box):")    #[0-9] or "\d"
# r=finditer(n,s)
# for i in r:
#     print(i.start(),i.group())


# string="qwertyu"
# pattern="qw"
# r=search(pattern,string)
# if r:
#      print("yes")
# else:
#   print("NO")


# STARTS WITH ENDS WITH

# string="qwertyu"
# pattern="^q"
# r=findall(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")


# string="qwertyu"
# pattern="u$"
# r=findall(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")



# STARTS WITH A WORD AND IN BTW WE CAN ADD ANYTHING BUT ENDS WITH THE GIVEN PATTERN

# string="qwerererfgrfcvxsdfgu"
# pattern="^q.*u$"
# r=findall(pattern,string)
# if r:
#     print("Yes.")
# else:
#     print("No.")


# Extract number from the string and add them to a list.

# string="qwert3456erty67"
# pattern="\d"
# r=finditer(pattern,string)
# for i in r:
#     if r:
#         print(i.group())
#     else:
#         print("Error.")


# OR

# string="qwert3456erty67"
# r=findall("\d+",string)
# print(r)


# SORT NUMBERS WHICH LENGTH IS EQUAL TO OR MORE THAN 3
# l=[]
# string="qwert3456erty67jnb6989hbhj987jnj9"
# r=findall("\d+",string)
# for i in r:
#     if len(i)>=3:
#         l.append(i)
#     # else:
#     #     print(r)
# print(l)


# EITHER OF THE ONE GIVEN IN A STRING 
# string="rtyujtF"
# pattern="[a-z][A-Z]|[0-9]"
# r=findall(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")



# string= "KL 05 H 1734"
# pattern= "^[A-Z]{2} [0-9]{2} [A-Z]{1,2} [0-9]{4}$"
# r=search(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")


# PAN CARD

# string="ASDFA7190K"
# pattern="^[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}$"
# r=findall(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")

# x=""
# string=["A","S","D","F","7","1","9","0","K"]
# pattern="^[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}$"
# s=input("Enter your surname:")
# string.insert(4,s[0])
# # print(string)
# for i in string:
#     x+=i
# print(x)
# r=findall(pattern,x)

# if r:
#     print("Number matches.")
# else:
#     print("Number does not matches.")



# IF A MOBILE MATCHES OR NOT
# string=input("Enter mobile number:")
# pattern="^([+]91)[0-9]{10}"
# r=fullmatch(pattern,string)
# if r:
#     print("yes")
# else:
#     print("no")