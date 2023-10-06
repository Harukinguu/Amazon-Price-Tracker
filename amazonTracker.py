import requests
from bs4 import BeautifulSoup

print("hello world")

amazonURL = "https://www.amazon.co.jp/Python%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%AF%E3%83%83%E3%82%AF%E3%83%96%E3%83%83%E3%82%AF-Chris-Albon/dp/4873118670/ref=sr_1_39?crid=35JUIBYOVM06Z&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1696131843&sprefix=python+orai%2Caps%2C170&sr=8-39"

def amazonTrackingPrice():
  amazonPage = requests.get(amazonURL)
  Soup = BeautifulSoup(amazonPage.content, "html.parser")
  # print(Soup)

  title = Soup.find(id="productTitle").get_text()
  price = Soup.find("span" , class_="a-size-base").get_text()
  converted_price = price[1:6].replace(",", "")
  int_price = int(converted_price)
  print(title)
  print(price)
  print(converted_price)

  if (int_price > 3000):
    sendLine()


def sendLine():
  print("Lineに通知を送ります")



amazonTrackingPrice()