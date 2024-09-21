class dog:
    #Attribute
    name = None
    age = None
    #Behaviour
    def __init__(self,name, age): #this is constructor
        self.name = name
        self.age = age

    def sleep(self):
        print('sleeping')
        print('Who is sleeping ->', self.name, "It's age is", self.age)


dog1 = dog("chow",10)
print(dog1.name)
dog1.sleep()




