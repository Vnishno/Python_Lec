inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grape"]

print(inventory.count("apple"))
print(inventory.index("orange"))


print(inventory)
inventory.extend(new_items)
print(inventory) 


print(inventory[::-1])