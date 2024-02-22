# API handeling
import requests

r = requests.get("https://fakestoreapi.com/products")
print(r.json() , r.status_code)