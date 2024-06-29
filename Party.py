# n = input("Name of the person you want to invite:")
# print(n,"has been invited to the party.")
# count=0
# m = input("Do you want to invite somebody else? yes or no.")
# while m=="yes":
#   n = ("Name of the person you want to invite:")
#   m = input("Do you want to invite somebody else? yes or no.")
#   count=count+1
# print("Thank you")
# print(count)

count=0
m = input("you want to invite? yes or no: ")
while m=="yes":
    n = input("enter the name:")
    print(n,"has been invited.")
    m = input("you want to invite somebody else? yes or no")
    count+=1
print("You invited",count,"people.")
print("Thank you")
 
   