from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

json_string = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data = json.loads(json_string)

product = Product(**data)

print("ტიპი:", type(product))
print("ობიექტი:", product)
print("სახელი:", product.name)
print("ფასი:", product.price)
print("მარაგშია:", product.in_stock)