#PyATB Students
#Attributes/ Properties/ Data Member
#Behaviour / Methods / Member functions


#Attributes - name, id, phoneNo, gender, colour_eyes, city, location, address (By which you recognize yourself
#Behaviour - walk, talk, write, sing, dance, watch, listen, sleep, cry, smile (I can do something)

#Blueprint from line 9 to 31
class person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phoneNo = None
    address = None
#Behaviour
    def talk(self): #NRNG #self -> this, Self wil be first argument in every behaviour
        print("I can talk")
    def sleep(self,name):
        print("I am a method!!") #Arg with no return
        print("Sleep",name)
    def sleep2(self,name):
        print("I am a method!!") #Arg with return
        return None
    def walk(self):
        print("I'm Walking") #No Return No Argument
    def walk_return(self):
        return "I'm walking" #No Arg with return


#Create an object of the class
#ObjectRef = className() -> Object

abhishek = person()
abhishek.name = 'Abhishek'
abhishek.talk()
