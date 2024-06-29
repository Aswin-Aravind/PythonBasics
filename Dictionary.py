#items() -> to print dictionary items.
# clear(),pop(),values(),keys(),get(),update(),len()



# students={"name":"aswin","age":"23","place":"kakkanad","name":"arya"}
# for i in students:
#     # print(i,students[i])
#     print(students.items())


# students={"name":"Aswin","age":"23","role":"student"}
# print(students)
# print(students.values())
# print(students.get("name"))
# students.pop("role")
# print(students)
# students["place"]="kakkanad"
# print(students)
# print(students.clear())
# print(list(students))
# new=[]
# for i in students:
#     new.append(i)
# print(new)


# sort favourite foods
# food={}
# for i in range(1,5):
#     name=input("Enter food name:")
#     food[i]=name
# print(food)
# print(food.keys())
# n=int(input("Which food you want to delete?"))
# food.pop(n)
# print(food)


# #or
# food={}
# l=["food1","food2","food3"]
# for i in l:
#     print(i)
#     name=input("Enter food name:")
#     food[i]=name
# print(food)
# rem=input("Remove food:")
# print(food.pop(rem))
# print(food)

# # print till the given key value.
# dict={1:"hello",2:"world",3:"hai",4:"abc"}
# for i in dict:
#    n=int(input("Enter the key value"))
#    if n == i:
#       print(dict(n))



# mean of results
# result={"jithin":60,"fayas":70,"aswin":75,"brightlee":60}
# print(sum(result.values())/len(result))


# print who all have below 50 and count of above 80.
# result={"a":60,"b":70,"c":75,"d":80,"e":90,"f":30,"g":85}
# count=0
# for i in result.values():
#  if i<50:
#  elif i>80:
#   count+=1 
# print(count)
#      print(result.keys())       
                

# data_dict = {"a": 60, "b": 40, "c": 90, "d": 35, "e": 85}

# # Removing entries below 50
# keys_to_remove = []
# for key, value in data_dict.items():
#     if value < 50:
#         keys_to_remove.append(key)

# for key in keys_to_remove:
#     del data_dict[key]

# # Counting entries above 80
# count_above_80 = 0
# for value in data_dict.values():
#     if value > 80:
#         count_above_80 += 1

# print("Dictionary after removing entries below 50:", data_dict)
# print("Count of entries with values above 80:", count_above_80)