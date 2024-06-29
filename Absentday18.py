# Dictionary

# text= "hello hai hello hai hai"
# dict={}
# n=text.split(' ')
# print(n)
# for i in n:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)


# first recursive character in the given string

# m="ABACBABCD"
# d=[]
# for i in m:
#     if i in d:
#         print("First recursive letter is",i)
#         break
#     else:
#         d.append(i)


# count the repeatation also print the strings which have the value 1.

# text="ABBCD"
# d={}
# for i in text:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# l=list(d.items())
# print(l)
# for i,j in l:
#     if j==1:
#      print(i)
#     # else:
    #     print("Get out!")


# a={"A":1,"B":2,"C":3,"D":4}
# b={"a":1,"b":2,"c":3,"d":4}
# b.update(a)
# print(b)


# FUNCTIONS
# eg: min(),max(),print(),input(),sum()

# example:

# def add(a,b):
#     return a+b
# k=add(10,6)
# print(k)

# def add(a,b,c):
#     return a+b+c
# k=add(10,1,2)
# print(k)


# return square value:

def sq(a):
    return a**2
k=sq(int(input("Enter the number:")))
print(k,"is the square.")