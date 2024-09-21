def make_pizza(*toppings):
    for topin in toppings:
        print(topin)

abhishek = make_pizza("FreshBase","Paneer")
tejas = make_pizza("Olives","Mushroom", "Tomato")

print(abhishek)
print(tejas)

def make_pizza(*toppings, base):
        print(toppings,base)

make_pizza("Paneer","Tomato",base="FreshBase")


