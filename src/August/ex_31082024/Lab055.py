"""
Create a employee class with constructor which has the following and with the help of constructor set the values
# Attributes : name,age, phoneNumber, address, empID
#Behaviour : walk, talk, printdetails
also ask the user about the information for emp1, emp2
finally print the details of emp1,emp2 via the print employee function
"""
class employee():
    #Attributes
    def __init__ (self,name,age,phoneNumber,address,empID):
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber
        self.address = address
        self.empID = empID

    #Behaviour
    def walk(self):
        print("I can Walk")

    def talk(self):
        print("I can talk")

    def printDetails(self):
        print(f"Employee Name is {self.name}, ID is {self.empID}, age is {self.age}, phone number is {self.phoneNumber}, address is {self.address}")
def getEmployeeDetails():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    phoneNumber = input("Please enter your phoneNumber: ")
    address = input("Please enter your address: ")
    empID = input("Please enter your empID: ")
    return employee(name,age,phoneNumber,address,empID)

print("Enter Employee 1 details: ")
employee1 = getEmployeeDetails()
print("Enter Employee 2 details: ")
employee2 = getEmployeeDetails()
print("Detail of employee 1 :")
employee1.printDetails()
print("Detail of employee 2 :")
employee2.printDetails()

