# API handeling
import requests

def productsdetails():
	r = requests.get("https://fakestoreapi.com/products")
	# print(r.json() , r.status_code)

	if r.status_code == 200:
		for product in r.json():
			print(product['title'])
	else:
		raise Exception("Fail to fetch")

# productsdetails()

def main():
	try:
		productsdetails()
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()