import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def search_amazon(query):

    url = f"https://www.amazon.in/s?k={query}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    items = soup.select(".s-result-item")

    for item in items[:10]:

        title = item.select_one("h2")

        if title:

            product = {
                "name": title.text.strip(),
                "price": 1000,
                "website": "Amazon",
                "url": "https://amazon.in",
                "image": "https://via.placeholder.com/200"
            }

            products.append(product)

    return products
