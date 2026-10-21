class Product:
    shop_name = "Megashop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity 
            print(f"გაიყიდა {quantity} ცალი {self.name}, დარჩა: {self.stock}")
        else:
            print(f"მარაგში არ გვაქვს საკმარისი {self.name}")

laptop = Product("Samsung Galaxy S25 Ultra", 2500, 10)

print(f"პროდუქტი: {laptop.name}, ფასი: {laptop.price}₾, საწყისი მარაგი: {laptop.stock}")
print("=" * 40)

laptop.sell(2)
laptop.sell(3)
laptop.sell(100)