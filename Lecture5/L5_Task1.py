attempt = 0 
pin=""

while attempt < 3:
    pin = int(input("Enter your PIN: "))

    if pin == 1234:
        print("Access granted!")
        break
    else:
        attempt += 1
        if attempt < 3:
            print(f"Incorrect PIN. Remaining attempts: {3-attempt}")
        else: 
            print("Card blocked!")
