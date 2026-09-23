correct_pin = 1234
balance = 1945.3
requested_amount = 1000
entered_pin = int(input("Enter your PIN: "))

if correct_pin == entered_pin:
    if requested_amount <= balance:
        print(f"Withdrawal successful! Remaining balance: ${balance-requested_amount}")
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")
 