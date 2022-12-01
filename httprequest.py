import requests

from bs4 import BeautifulSoup

from csv import writer


response=requests.get("http://quotes.toscrape.com/")
soup=BeautifulSoup(response.text,"html.parser")
s=soup.find_all(class_="text")
for i in s:
    print(i.get_text())