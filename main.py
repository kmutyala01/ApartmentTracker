
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import smtplib


def get_price():
    url = "https://www.apartments.com/two99-monroe-roanoke-tx/xgb8vqm/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    response = requests.get(url, headers=headers)



    soup = BeautifulSoup(response.content,'html.parser')

    apartment_info = soup.find_all('h3', class_ = "modelLabel")
    for apartment in apartment_info:
        curr = apartment.text.split("$")

        modelName = curr[0].split(" ")[0].split('\n')[1]  #Parsing model name of apartment
        
        
        if modelName == "A1":
            price = curr[1].split("–")[0][:-1] #Parsing price of apartment 
            price = price.split(",") #Removing comma
            price = int(''.join(price[0 : 2])) 
            if price <= 2500:
                notify("https://www.apartments.com/two99-monroe-roanoke-tx/xgb8vqm/", price)






def notify(link,price):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("notifierapt@gmail.com", "Karthik1234")
    message = "Hey! it is now " + str(price) + "\n" + link
    server.sendmail("notifierapt@gmail.com", "karthiksatya@gmail.com", message )
    server.quit()


while True:
    get_price()
    time.sleep(60 * 60 * 6) #6 hours

