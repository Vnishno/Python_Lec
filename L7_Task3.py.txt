fruits = ["apple", "banana", "cherry", "orange"]

try:
    user_input = int(input("Enter an index number: "))
    selected_fruit = fruits[user_input]
    print(f"Selected fruit: {selected_fruit}")

except ValueError:
    print("Invalid input! Please enter a whole number.")

except IndexError:
    print(f"Index out of bounds! Choose an index between 0 and {len(fruits)-1}.")

else:
    print("Successfully retrieved item!")