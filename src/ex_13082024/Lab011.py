#Strings

name = "Abhishek"
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a = print(type("90"))
age = print(type(90))

newLine = "This is a big line"
print(newLine)
newLine = newLine + str(1)
print(newLine)

firstName = 'Abhishek'
lastName = 'Birur'

fullName = firstName + lastName #Concat
print(fullName)

howManyPlanesiHave = None
print(type(howManyPlanesiHave))

#id

age = 10
age2 =10
print(id(age)) #prints the address of memory location,
print(id(age2)) #prints the address of memory location,
# Since value of age and age2 are same, It returns same memory location, Just to save the memory for best usage of memory
