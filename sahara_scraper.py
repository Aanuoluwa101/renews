from bs4 import BeautifulSoup
import requests

html = requests.get("https://saharareporters.com/").text

soup = BeautifulSoup(html, "html.parser")

titles = soup.findAll("h2", {"class": "title"})
links = [title.find("a")["href"] for title in titles]

news_html = requests.get("https://saharareporters.com/2023/08/27/nigerian-air-force-aircraft-departs-abuja-paris-amid-niger-political-crisis")

soup2 = BeautifulSoup(news_html, "html.parser")

print(soup2.prettify())