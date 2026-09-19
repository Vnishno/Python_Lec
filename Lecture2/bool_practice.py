number = input("Enter your number: ")
num=int(number)

is_positive = num > 0 
is_negative = num < 0 
is_zero = num == 0 

is_even = num % 2 ==0
is_odd = num % 2 != 0

print("Is positive:",is_positive)
print("Is negative:",is_negative)
print("Is zero:",is_zero)
print("Is even:",is_even)
print("Is odd:",is_odd)