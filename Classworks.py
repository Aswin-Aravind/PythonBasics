days=365.25
weeks=52
months=12
years=100
n=float(input("Enter your age?"))
while True:
    print("You have left",years-n,"years, then",(years-n)*weeks,"weeks, then",(years-n)*months,"months and",(years-n)*days,"days.")
    print((years-n)*days*24,"hours then",(years-n)*days*24*60,"minutes and",(years-n)*24*60*60,"seconds left.")
    break



# pwd=input("Enter password:")
# # while True:
# for i in pwd:
#  if len(pwd)>7 and len(pwd)<15:
#     if i=="1" or i=="2" in pwd:
#         if i=="@" or i=="#" in pwd:
#             print("Password Accepted.")      #homework
#            #  break
# else:
#     print("Password unacceptable.")
#    #  break

