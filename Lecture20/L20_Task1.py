from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product1 = Product(name="Macbook", price=2500.0, in_stock=True)
product2 = Product(name="Mouse", price=75.5, in_stock=True)
product3 = Product(name="Keyboard", price=120.0, in_stock=False)

print(product1)
print(product2)
print(product3)