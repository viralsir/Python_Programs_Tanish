class student:
    rollno=0
    name="amit"

    # def __init__(self):
    #     self.rollno=0
    #     self.name=""

    def entry(self):
        self.rollno=int(input("enter your rollno"))
        self.name=input("enter your name")


    def display(self):
        print(self.rollno,self.name)



# student1=student()
# # student1.rollno=23
# # print(student1.rollno)
# # print(student1.name)
# student1.entry()
# student1.display()
studentlist=[]
for i in range(2):
    student1=student()
    student1.entry()
    studentlist.append(student1)

for student in studentlist:
    student.display()











