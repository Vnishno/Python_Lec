import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = 'https://crudcrud.com/api/c59b847b0ce34ae5a4d2756b78c7b1b6'

try:
    response = requests.get(f'{BASE_URL}/products', timeout=10)
    
    response.raise_for_status()
    
    products = response.json()
    
    for product in products:
        product_id = product.get('_id')
        name = product.get('name')
        price = product.get('price')
        
        print(f"ID: {product_id}")
        print(f"სახელი: {name}")
        print(f"ფასი: {price} ლარი")
        print("=" * 40)

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")
