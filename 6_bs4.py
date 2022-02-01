import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.a["href"]) 

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class ="Nbtn_upload" 인 a element를 찾아줘
#print(soup.find( attrs={"class":"Nbtn_upload"})) #class ="Nbtn_upload" 인 어떤 element를 찾아줘
rank1 = soup.find("li", attrs={"class":"rank01"})
# #print (rank1.a.get_text())
# rank2 = (rank1.find_next_sibling("li"))
# print (rank2.a.get_text())
# rank3 = (rank2.find_next_sibling("li"))
# print (rank3.a.get_text())

# rank2 = rank1.find_next_siblings("li")
# print(rank2)
webtoon = soup.find("a", text="나노마신")
print(webtoon)