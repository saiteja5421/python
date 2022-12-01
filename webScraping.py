import requests
import bs4
url1="/page/1"
url="http://quotes.toscrape.com/"
authors=set()
while url1:
	result =requests.get(f'{url}{url1}')
	soup=bs4.BeautifulSoup(result.text,"lxml")
	author =soup.select(".author")
	for n in author:
		authors.add(n.text)
	m=soup.find(class_='next')
	if m:
		url1=m.find("a")["href"] 
	else:
		url1=None
for a in authors:
	print(a)

# def solve(a,b):
# 	return b if a==0 else solve(b%a,a)
# print(solve(20,50))
# print(50%20)