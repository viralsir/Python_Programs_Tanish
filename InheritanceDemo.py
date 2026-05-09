class personal_info:
    id=0
    name=""
    phone_number=""

    def setPersonal_info(self):
        self.id=int(input("enter id :"))
        self.name=input("enter name :")
        self.phone_number=input("enter phone number :")

    def getPersonal_info(self):
        print("id:",self.id)
        print("name:",self.name)
        print("phone number:",self.phone_number)

class Employee(personal_info):
    salary=0

    def setSalary(self):
        self.salary=int(input("enter salary :"))

    def getSalary(self):
        print("salary:",self.salary)



class Dmart(Employee):
    location=""

    def setDmart(self):
        self.setPersonal_info()
        self.setSalary()
        self.location=input("enter dmart location :")

    def getDmart(self):
        self.getPersonal_info()
        self.getSalary()
        print("dmart:",self.location)

class Customer(personal_info,Dmart):
    billno=0
    billamount=0

    def setCustomer_billno(self):
        self.billno=int(input("enter billno :"))
        self.billmount=int(input("enter billmount :"))

    def getCustomer_billno(self):
        print("billno:",self.billno)
        print("billmount:",self.billmount)


#single inheritance
# emp1=Employee()
# emp1.setPersonal_info()
# emp1.setSalary()
#
# emp1.getPersonal_info()
# emp1.getSalary()

#multilevel inheritance
# dmart1=Dmart()
# dmart1.setDmart()
# dmart1.getDmart()

#hyrarchial inheritance
emp1=Employee()
emp1.setPersonal_info()
emp1.setSalary()

cust1=Customer()
cust1.setPersonal_info()
cust1.setCustomer_billno()


