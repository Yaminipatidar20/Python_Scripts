class Student:
    def get_data(self):
        self.name=input("Enter Your Name:-")
        self.address=input("Enter Your Address:-")
        self.state=input("Enter Your State Name:-")
        self.number=input("Enter Your Telephone Number:-")
        self.clgname=input("Enter Your College Name:-")
        self.clgads=input("Enter Your College Address:- ")
    def show_data(self):
        print("Your Name is:-",self.name)
        print("Your Address is:-",self.address)
        print("Your State name is:-",self.state)
        print("Your Telephone Number is:-",self.number)
        print("Your College Name is:-",self.clgname)
        print("Your College Address is:-",self.clgads)
s1=Student()
s1.get_data()
s1.show_data()



