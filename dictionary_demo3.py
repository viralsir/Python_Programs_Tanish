studentlist=[]
title_list=["RollNo:","Name:","Maths:","Science:","English:","Chemistry:"]
option1=0
while option1!=3:
    print("\t\t\t Student Info")
    print("\t\t press 1 for Entry")
    print("\t\t press 2 for View")
    print("\t\t press 3 for Exit")

    option1=int(input("Enter the option: "))
    if option1==1:
        option2='y'
        while option2=='y' or option2=='Y':
            print("\t\t\t Entry")
            student={}
            for title in title_list:
                if title=="RollNo:" or title=="Name:" :
                    student[title]=input("Enter the"+title+":")
                else :
                    student[title]=int(input("Enter the"+title+":"))
            studentlist.append(student)
            option2=input("Do you want to Continue? (y/n) : ")

    elif option1==2:
        print("\t\t\t View")

        for student in studentlist:
            isPass=True;
            for title,value in student.items():
                print(title,value)
                if title!="RollNo:" and title!="Name:" :
                    if value<34:
                        isPass=False
            if isPass==True:
                print("You are pass")
                # print("total :", sum(student[2:]))
                # print("avg:", sum(student[2:])/len(student[2:]))

            else :
                print("You are Fail")


            print("===================")
    elif option1==3:
        print("\t\t\t You are Exit")
    else :
        print("\t\t\t Invalid Option try again")
