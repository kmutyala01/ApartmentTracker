
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time


url = "https://www.apartments.com/ave-las-colinas-irving-tx/qfsptny/"
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
response = requests.get(url, headers=headers)

print(response)

soup = BeautifulSoup(response.content,'html.parser')

price_response = soup.find_all('span',class_ = "rentLabel")
print(len(price_response))
all_prices = []

for price in price_response:
    curr = price.text.strip()
    print(curr)
    #if curr[0] == "$":
    #     ch = curr[6:10]
    #     all_prices.extend(curr[1:].split(ch))

    # print(price.text.strip())
#     print(len(price.text.strip()))
    # print('*****')
