import requests
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = 'https://crudcrud.com/api/c59b847b0ce34ae5a4d2756b78c7b1b6'

product_data = {
    "name": "Laptop", 
    "price": 2500, 
    "in_stock": True
}

try:
    response = requests.post(f'{BASE_URL}/products', json=product_data, timeout=10)
    
    response.raise_for_status()
    
    print("Status Code:", response.status_code)
    
    print("Server Response:", response.json())

except HTTPError as e:
    print(e)

except ConnectTimeout as e:
    print("Server took too long")
