import requests
from bs4 import BeautifulSoup
import smtplib
#import time

URL = "https://www.ebay.co.uk/itm/Inspire-Fitness-CB1-Air-Bike-Exercise-CrossFit-Airdyne-Assault-Bike-Gym-Cardio/401529330033?hash=item5d7d035971:g:weUAAOSwjB9a5B7u"

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="itemTitle").get_text()
    parsed_title = title[13:] # ebay seems to print Details about before every title!
    print("The observed item is: ", parsed_title.strip())

    price = soup.find(id="prcIsum").get_text()
    price = price[1:-3]
    converted_price = float(price)
    print("The item's current price is: ", converted_price)

    if converted_price < 400.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("katharina.education@gmail.com", "dymacfhabmsbswwt")

    subject = "Price dropped down!"
    body = "Check the eBay link https://www.ebay.co.uk/itm/Inspire-Fitness-CB1-Air-Bike-Exercise-CrossFit-Airdyne-Assault-Bike-Gym-Cardio/401529330033?hash=item5d7d035971:g:weUAAOSwjB9a5B7u"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
    "katharina.education@gmail.com",
    "katharina.education@gmail.com",
    msg
    )
    print("THE EMAIL HAS BEEN SENT!")
    server.quit()

check_price()

# while True:
#     check_price()
#     time.sleep(120)
