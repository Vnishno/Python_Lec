cart_total = 60
is_vip = True
is_guest = False
promo_code = "SAVE10"

if cart_total >= 50 or is_vip:
    print("You got free shipping")
else: 
    print("You need to pay for shipping")

if promo_code  and not is_guest:
    print(f"You got 10% discount your final price is {cart_total*0.9}")
else:
    print(f"Your final price is {cart_total}")