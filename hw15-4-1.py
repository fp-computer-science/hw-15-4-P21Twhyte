# Tow 2/9/2021

def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
    return inventory    


new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory) # Should return True
print(new_inventory["strawberries"] == 10) # Should return True
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35) # Should return True