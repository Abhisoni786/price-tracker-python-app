import smtplib

import requests
from bs4 import BeautifulSoup


def amazon_price_tracker():
	url = input("Provide the full url of the product link: \n")

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	get_price = soup.find(id="priceblock_ourprice").get_text()

	updated_price = int(get_price[1:5])
	print(
		f"\nYour product is {title.strip()} and it's price is {updated_price}")

	mini_price = int(input("\nProvide the minimum price that you want: "))
	if updated_price <= mini_price:
		send_mail(url)
	else:
		print("Price is same as before!")


def flipkart_price_tracker():
	url = input("Provide the full url of the product link: \n")

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(class_="_35KyD6").get_text()
	
	get_price = soup.find(class_="_3qQ9m1").get_text()
	wc_price = get_price.replace(",","")

	print(wc_price)

	updated_price = int(wc_price[1:5])
	print(
		f"\nYour product is {title.strip()} and it's price is {wc_price}")

	mini_price = int(input("\nProvide the minimum price that you want: "))
	if updated_price <= mini_price:
		send_mail(url)
	else:
		print("Price is same as before!")



def send_mail(link):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('abhisoni883@gmail.com', 'dzvcfldmedbwxlhw')

	subject = "PRICE FALL DOWN"
	body = "Check the Link \n "+link

	msg = f"Subject: {subject}\n\n{body}"
	
	server.sendmail("abhisoni883@gmail.com","support@trustable.co.in",msg) 
	print("HEY Mail has been sent to your email address!") 
	server.quit()




###### Main site Codes

print("\n\t\t\t\t\t\tWelcome to price tracker Demo\n\nSelect your site: ")

print("1.Amazon\n2.Flipkart")

site = int(input("Type the number eg 1 :- "))
print(site)

if (site == 1):
	amazon_price_tracker()
elif site == 2:
	flipkart_price_tracker()

else:
	print('wrong typo')
