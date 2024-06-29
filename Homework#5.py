# Using List comprehension 
# 1.To print square in the range 5-50

# def squares(start,end):
#     squares=[i**2 for i in range(start,end+1)]
#     return squares
# print(squares(5,50))

# or

# squares=[i**2 for i in range(5,51)]
# print(squares)


# 2.To print cube in the range 1-10

# cubes=[(i,i**3) for i in range(1,11)]
# print(cubes)

# or

# n=[]
# for i in range(1,11):
#     n.append((i,i**3))
# print(n)


# 3.string='Luminar Technolab'  
#  A)string vowels count
#  B)not vowels count

# string="Luminar Technolab"
# vowel_count=[i for i in string if i in "aeiou"]
# non_vowel_count=[i for i in string if i not in "aeiou"]
# print("There are",len(vowel_count),"vowels in the string.")
# print("There are",len(non_vowel_count),"non vowels in the string.")

# or

# string="Luminar Technolab"
# vowel_count=0
# non_vowel_count=0
# vowel="aeiou"
# for i in string:
#     if i not in vowel:
#         vowel_count+=1
#     else:
#         non_vowel_count+=1
# print("Non-vowels are",non_vowel_count)
# print("Vowels are",vowel_count)


# 4. 50 to 1000 range fin multiplication count of 5

# count = [i for i in range(50,1001) if i%5==0]
# print(count)

# or

# m=[]
# for i in range(50,1001):
#     if i%5==0:
#         m.append(i)
# print(m)


# 5.lst=[2,4,6,8,10,12,14,15]
# A)Square of each element in list,if the square is above 50 #Output should like pairs
# 	output=[2,4,5,(8,64),(10,100),.....]

# lst=[2,4,6,8,10,12,14,15]
# squares_lessthan50=[(i**2) for i in lst if i**2<50]
# squares_morethan50=[(i,i**2) for i in lst if i**2>50]
# print(squares_lessthan50+squares_morethan50)

# # or
# lst=[2,4,6,8,10,12,14,15]
# l=[]
# a=[]
# for x in lst:
#     if x**2<50:
#         l.append(x**2)
#     elif x**2>50:
#         a.append((x,x**2))
# print(l+a)