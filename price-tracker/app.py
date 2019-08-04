import requests
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.in/Ant-Audio-Thump-560-Headphone/dp/B07KTP84LM/ref=sr_1_1_sspa?crid=3DU418L6GYMZJ&keywords=ant+audio+thump+560&qid=1564853263&s=gateway&sprefix=ant+audio+th%2Caps%2C769&sr=8-1-spons&psc=1"


# check price
def check_price():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").get_text()

    updated_price = int(price[1:5])

    print(updated_price)
    if(updated_price<=275):
        send_mail()
        
    else:
        print(f"Price still same as previous \n\nold price:- {updated_price}")  

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abhisoni883@gmail.com', 'dzvcfldmedbwxlhw')

    subject = "PRICE FALL DOWN"
    body = "Check the amazon "+url

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail("abhisoni883@gmail.com","support@trustable.co.in",msg) 
    print("HEY Mail has been sent to your email address!") 
    server.quit()



check_price()