import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0"
}

def search_amazon(query):

    url = f"https://www.amazon.in/s?k={query}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    products = []

    items = soup.select(".s-result-item")

    for item in items:

        title = item.select_one("h2")
        price = item.select_one(".a-price-whole")
        image = item.select_one("img")

        if title and price and image:

            product = {
                "name": title.text.strip(),
                "price": int(price.text.replace(",","")),
                "website":"Amazon",
                "url":"https://www.amazon.in",
                "image": image["src"]
            }

            products.append(product)

    return products
