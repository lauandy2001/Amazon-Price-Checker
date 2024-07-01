import requests
import smtplib
from bs4 import BeautifulSoup

def check_price:

    URL = "https://www.amazon.com/VIVAGLORY-Flotation-Durable-Adjustable-Fastening/dp/B07QTPB1F1/?_encoding=UTF8&pd_rd_w=4fqxG&content-id=amzn1.sym.e92d427b-6681-44e4-9201-8463289b9c75%3Aamzn1.symc.f3a6ae52-fb92-4bbd-ba18-628777ebc1c0&pf_rd_p=e92d427b-6681-44e4-9201-8463289b9c75&pf_rd_r=QJEB7PZ8S33J0JP1B7HX&pd_rd_wg=85Qre&pd_rd_r=1ac3bcc0-b80d-4d94-97bb-9dc1d461b6a7&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d'}
    headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"} 

    AmazonPage = requests.get(URL,headers = headers)

    soupInfo = BeautifulSoup(AmazonPage.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price1 = soup.find(class = 'a-price-whole').get_text()
    price2 = soup.find(class = 'a-price-fraction').get_text()
    
    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())


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
