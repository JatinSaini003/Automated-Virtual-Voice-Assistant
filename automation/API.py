import requests as r
from bs4 import BeautifulSoup as bs

link = "https://www.google.com/search?q=temperature"
data = bs(r.get(link).text, "html.parser")
temp = data.find("div", class_="BNeawe").text
print(temp)