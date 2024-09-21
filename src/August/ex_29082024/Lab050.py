student_information = {
    "Name" : "Abhishek",
    "Age" : 27,
    "Address": 'KA'
}
#Other way of writing this code

student_information2 = dict(name = 'Tejas', age = 23, address = 'KA')

print(student_information)
print(type(student_information))
print(student_information['Name'])
print(student_information['Age'])
print(student_information['Address'])
print('------------------------------------')
print(student_information2)
print(type(student_information2))
print(student_information2['name'])
print(student_information2['age'])
print(student_information2['address'])