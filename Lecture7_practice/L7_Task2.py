password = input("Enter password: ")

try:
    if len(password) < 6:
        raise ValueError("Password is short")
    else:
        print("Password accepted")
except ValueError as e:
    print(e)