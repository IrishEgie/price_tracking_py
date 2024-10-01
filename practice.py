from bs4 import BeautifulSoup
import os
import smtplib
import requests as rq
from datetime import datetime as dt


# Practice
url = "https://appbrewery.github.io/instant_pot/"
# Live Site
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {"Accept-Language":"en-US",
          "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

def send_email(message):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL_ADDRESS"),password=os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("EMAIL_ADDRESS"),to_addrs=os.getenv("SEND_TO"), msg=message)
    print(f"Email sent to {os.getenv("SEND_TO")} on {dt.now()}")





response = rq.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

# Find the HTML element that contains the price
item_price = soup.find(class_="a-offscreen").getText()
# Get the product title
title = soup.find(id="productTitle").get_text().strip()
# print(title)

# Remove the dollar sign using split
price_without_currency = item_price.split("$")[1]

price = float(price_without_currency)

print(price)

if price < 80:
    message = f"{title} is on sale for {price}!"
    send_email(message=message)