import requests
import smtplib
import time
from bs4 import BeautifulSoup



URL = 'https://www.amazon.com/Kuoser-Reflective-Adjustable-Visibility-Lifesaver/dp/B091TN8WWK/ref=sr_1_2?crid=2C2TXYBIR0Z3B&dib=eyJ2IjoiMSJ9.zGd3lLBP-XL6Od1rvDaUMRzKXqWruLeePk7J-oRVED9W9QWqM1wKAW_9iotCvY_FrXN5ucbkxr-bPTmLF4Z0nV8l1lJn0LIYH8nN9sU22po2Tq-Xsc7Ly27POqr88zcLAtsK8HQOyq8KXIrmrjoiGJXtA0UuwMIta_wePqhjrNFvt90jC_bf3nwh0_3ySgYmVxDWHGiXefx8RtjY7dDV-tatmc1VvF6WrIayvtT3yHUWjt10MtX2EfUNutdlpvlhycnr_SUJicXqE-R1gHH299AZmhSpGhwaTNLK5lxoHGU.Hyd2FCAsC9kWdBXVt-1j6FWYEDqbU49zMWNMdX5tAWo&dib_tag=se&keywords=dog+life+vest+xl&qid=1719964677&sr=8-2'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'} 

page = requests.get(URL,headers = headers)


deal_price = None
def get_price():
    global deal_price
    soup = BeautifulSoup(page.content,'html.parser')
    deal_price = soup.select_one(".a-offscreen").getText()
    print(deal_price)

while deal_price is None:
    try:
        get_price()
    except AttributeError:
        print("Error fetching price. Retrying...")
        time.sleep(5)  # Adding a delay of 5 seconds before retrying
'''
    AmazonPage.raise_for_status()
    data = AmazonPage.text
    print(data)

    soupInfo = BeautifulSoup(AmazonPage.content, 'html.parser')
    title = soupInfo.find(id='productTitle').get_text()
    #price1 = soupInfo.find(class_= "a-price-whole").get_text()
    #price2 = soupInfo.find(class_= "a-price-fraction").get_text()

    print(title)

while title is None:
    try:
        get_price()
    except AttributeError:
        print("Error fetching price. Retrying...")
        time.sleep(5)  # Adding a delay of 5 seconds before retrying

    
   
    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())
'''

def send_mail()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('lauandy2001@gmail.com',password) #two step verification

    subject = "Price fell down!"
    body = f"check the amazon link: {URL}"

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'lauandy2001@gmail.com',
        'lauandy2001@gmail.com',
        msg
    )
    print("Mail sent")

    server.quit()


