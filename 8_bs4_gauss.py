import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class": "title"})
ratings =soup.find_all("div", attrs={"class" : "rating_type"})
# title = cartoons[3].a.get_text()
# link = cartoons[0].a["href"]
# print("https://comic.naver.com"+link)

for cartoon in cartoons:
  title = cartoon.a.get_text()
  link = "https://comic.naver.com" + cartoon.a["href"]
  print(title,link)
  
  for rate in ratings:
    rates = rate.strong.get_text()
    print(title,link,rates)