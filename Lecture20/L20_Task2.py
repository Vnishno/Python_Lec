from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

product1 = Product(name="Macbook", price=2500.0, in_stock=True)
product2 = Product(name="Mouse", price=75.5, in_stock=True)
product3 = Product(name="Keyboard", price=120.0, in_stock=False)

products = [product1, product2, product3]

products_dict = [asdict(p) for p in products]

json_data = json.dumps(products_dict)
print(json_data)