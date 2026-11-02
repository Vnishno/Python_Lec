import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = 'https://crudcrud.com/api/c59b847b0ce34ae5a4d2756b78c7b1b6'

try:
    product_id = '6ae8d0eaa84d6103e80bf3d7'
    
    response = requests.get(f'{BASE_URL}/products/{product_id}', timeout=10)
    response.raise_for_status()
    
    product_data = response.json()
    
    print(f"ID: {product_data.get('_id')}")
    print(f"სახელი: {product_data.get('name')}")
    print(f"ფასი: {product_data.get('price')}")
    print(f"მარაგშია: {product_data.get('in_stock')}")

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")
