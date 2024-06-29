l=[1,2,3,4,4,5]
for i in range(1,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])
            break