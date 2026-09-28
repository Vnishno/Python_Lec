try:
    b_year = int(input("Enter your birth year: "))
    age = 2026 - b_year
    print(age)
except ValueError:
    print("Please enter digits")