my_shopping_list = ["WheyProtein","Creatine","IsolateProtein"]

print(my_shopping_list[0])
print(len(my_shopping_list))

def more_shopping(my_new_list):
    more_item = input("What supplement are you looking for ? ")
    my_new_list.append(more_item)
    #my_new_list.remove(more_item) #To remove something from the list
    #my_new_list.insert(0, more_items) #To insert at certain positionS
    return my_new_list

l = more_shopping(my_shopping_list)
print(l)