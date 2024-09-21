class dog:
    #Attribute
    name = None
    breed = None
    color = None
    #Behaviour
    def sleep(self):
        print("Sleeping")
    def bark(self):
        print("Barking")
    def eat(self):
        print("Eating")

dog1 = dog()
print(dog1.name)
dog1.name = 'Ruby'
print(dog1.name)
dog1.breed='Labrador'
print(dog1.breed)
dog1.color='Golden'
print(dog1.color)
dog1.sleep()

dog2 = dog()
print(dog2.name)
dog2.name = 'Kariya'
print(dog2.name)
dog2.breed='German Shepherd'
print(dog2.breed)
dog2.color='Black & Brown'
print(dog2.color)
dog2.bark()
