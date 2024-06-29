# party=[]
# count=3
# for i in range(3):
#     n=input("Enter the name:")
#     party.append(n)

# while True:
#     n=input("Do you want more people? y/n:")
#     if n=="y":
#         m=input("Add the name:")
#         count+=1
#     else:
#         print(count,"people are invited to the party.")
#         break
# print(party)

# # altering
# party=[]
# count=3
# for i in range(3):
#     n=input("Enter the name:")
#     party.append(n)

# while True:
#     n=input("Do you want more people? y/n:")
#     if n=="y":
#         m=input("Add the name:")
#         count+=1
#         party.append(m)
#     else:
#         print(count,"people are invited to the party.")
#         break

# print(party)
# m=input("Enter one name which is already in this list:")
# while True:
#     a=input("Do you still want to invite him. y/n:")
#     if a=="y":
#         print("Okay")
#     else:
#         party.remove(m)
#     print(party)
#     break

# or

party=[]
for i in range(3):
    n=input("Enter the name:")
    party.append(n)
m = input("Do you want to invite others? y/n:")
while m== "y":
    if m=="y":
         x=input("Enter the name:")
         party.append(x)
    else:
        print(len(party),"are invited.")




