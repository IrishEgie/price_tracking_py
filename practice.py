from bs4 import BeautifulSoup
import requests as rq

response = rq.get("https://appbrewery.github.io/instant_pot/")

soup = BeautifulSoup(response.text, "html.parser")

# Find the HTML element that contains the price
item_price = soup.find(class_="a-offscreen").getText()

# Remove the dollar sign using split
price_without_currency = item_price.split("$")[1]

price = float(price_without_currency)

print(price)