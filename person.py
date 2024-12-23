class Student():
    name=""
    age=12
    schoolclass="6th A"
    house="Sapphire"
    classteacher="Aswathy mam"

    def __init__(self):
        print("Making new student")

    def change_details(self):
        print("Please enter your age")
        self.age=int(input())
        print("Please enter the name of student")
        self.name=input()
    def show_details(self):
        print("the details of student are: ")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)

Student1=Student()
Student1.change_details()
Student1.show_details()
Student2=Student()
Student2.change_details()
Student2.show_details()
