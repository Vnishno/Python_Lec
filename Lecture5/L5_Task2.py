
entered_number = int(input("Enter positive integer: "))
total = 0

for i in range(2, entered_number+1,2):
    total += i

print(f"The sum of even numbers from 1 to {entered_number} is: {total}")