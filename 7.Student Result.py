BDA =eval(input("Enter Marks of Big Data Analytics:-"))
SEM =eval(input("Enter Marks Of Software Engeering:-"))
DS =eval(input("Enter Marks of Data Structure:-"))
DS1 =eval(input("Enter Marks of Data Science:-"))
PYTHON =eval(input("Enter Marks of Python:-"))
total =(BDA+SEM+DS+DS1+PYTHON)
avg =total/5
print("Total Marks Of Student:-",total)
print("Percantages of Student:-",avg)
if(avg>=85):
    print("Grade:-A+")
elif(avg>=75):
    print("Grade:-A")
elif(avg>=65):
    print("Grade:-B")
elif(avg>=55):
    print("Grade:-C")
elif(avg>=45):
    print("Grade:-D")
else:
    print("Grade:-E")

