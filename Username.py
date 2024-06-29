n = input("Enter the first name:")
if len(n)<5:
    m = input("Enter the second name:")
    p = n+"\t"+m
    print(p.upper())
elif len(n)>=5:
    print(n.lower())
else:
    print("Error.")
    