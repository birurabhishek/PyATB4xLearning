my_tuple = ('tta.com','sdet.live')
print(my_tuple)
print(type(my_tuple))
print('---------------------------------')
my_tuple_to_list = list(my_tuple)
print(my_tuple_to_list)
print(type(my_tuple_to_list))

print('---------------------------------')
hero1 = ('Batman','Bruce Wayne')
hero2 = ('WonderWomen','Diana Prince')

newHero = (hero1,hero2)

print(newHero)
print(newHero[0]) #'Batman','Bruce Wayne'
print(newHero[0][0]) #Batman
print(newHero[1][1]) #Diana Prince
print('---------------------------------')
#Search in Tuple
cities = ('London','Paris','Tokyo')
print("Paris" in cities)
print("Bengaluru" in cities)