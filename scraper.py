import requests

def search_amazon(query):

    url = f"https://dummyjson.com/products/search?q={query}"

    r = requests.get(url)

    data = r.json()

    products = []

    for item in data["products"]:

        product = {
            "name": item["title"],
            "price": item["price"],
            "website": "Online Store",
            "url": "https://dummyjson.com",
            "image": item["thumbnail"]
        }

        products.append(product)

    return products
