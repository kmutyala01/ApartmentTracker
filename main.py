
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time


url = "https://www.apartments.com/two99-monroe-roanoke-tx/xgb8vqm/"
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
response = requests.get(url, headers=headers)

print(response)

soup = BeautifulSoup(response.content,'html.parser')
model_response = soup.find_all('span', class_ = "modelName")
price_response = soup.find_all('span',class_ = "rentLabel")
apartment_info = soup.find_all('h3', class_ = "modelLabel")
all_prices = []
#print(price_response)
model_prices = {}

def notify():
    print("email sent")
    


for apartment in apartment_info:
    curr = apartment.text.split("$")

    modelName = curr[0].split(" ")[0].split('\n')[1]
    
    print(modelName)
    if modelName == "A1":
        price = curr[1].split("–")[0][:-1]
        price = price.split(",")
        price = int(''.join(price[0 : 2]))
        if price <= 1500:
            notify()


