import circle as c
import rectangle as r
choice=0
ch='y'
while(ch=='y'):
    print("MENU")
    print("_____________________________________________")
    print("(1) Area of circle")
    print("(2) Circumference of a circle")
    print("(3) Area of Rectangle")
    print("(4) Perimeter of rectangle")
    print("(5) Exit")
    print("______________________________________________")
    choice=int(input("Enter the Choice:-"))
    if (choice==1):
        radius=eval(input("Enter the circle radius:-"))
        print("The area is:-",c.area(radius))
    elif (choice==2):
        radius=eval(input("Enter the circle radius:-"))
        print("The circumference is:-",c.circumference(radius))
    elif (choice==3):
        w=eval(input("Enter the Rectangle width:-"))
        l=eval(input("Enter the Rectangle lenth:-"))
        print("The Area is:-",r.area(w,l))
    elif (choice==4):
        w=eval(input("Enter the Rectangle width:-"))
        l=eval(input("Enter the Rectangle lenth:-"))
        print("The perimeter is:-",r.perimeter(w,l))
    elif(choice==5):
        print("Thanks For Using This Application")
        quit()
    else:
        print("ERROR:INVALID CHOICE")

