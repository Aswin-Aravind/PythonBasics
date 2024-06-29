# File Operatons
# create, read, update, delete, CRUD


# file=open("new.txt")       #file=open("new.txt","rt")  storing a file to a variable "file" by "r" reading the "t" text file.
# print(file.read())         #read - r
                           
                           #write - w
                           
                           #append - a

                           #create - x

# open() - is the main function in fileoperations.
          #open() - which should contain two parameters ; filename,mode
          #eg - variable = open(file_name, mode)


file=open("aswin.txt","w")
file.write("hello aswin")
print(file.read())