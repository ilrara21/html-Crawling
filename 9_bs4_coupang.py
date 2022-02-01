import requests


import re 
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?rocketAll=false&q=%EB%A7%A5%EB%B6%81&brand=42308&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=376&component=&rating=0&sorter=scoreDesc&listSize=36"

headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(res.text)
for item in items:
  name = item.find("div", attrs={"class" : "name"}).get_text()
  price = item.find("strong", attrs={"class" : "price-value"}).get_text()

  rate = item.find("em", attrs={"class" : "rating"}) #평점
  if rate:
    rate=rate.get_text()
  else :
    rate = "평점없음"
  rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
  if rate_cnt :
    rate_cnt=rate_cnt.get_text()
    rate_cnt=rate_cnt[1:-1]
  else :
    print("평점없는 상품은 제외")  
    
  # 1테라 제품 제외
  if "1024" in name:
    print("이건 ssd 용량이 좀 과해서 제외")
    continue
  
  
  # ssd 256도 제외    
  if "256" in name:
    print("이건 용량이 적어서 못쓴다")
    continue
    
    
  if float(rate) >=4.5 and int(rate_cnt) >=1000 :
    print(name,":" ,price,":","평점",rate, ":","리뷰수", rate_cnt)
  else :
    print(rate_cnt,"(","리뷰수가 모자라네요. 힘내세요",")")

  
  


# items = name+price
# for item in items:
  
#   name = item.find_all("div", attrs={"class" : "name"})
#   price= item.find_all("strong", attrs={"class" : "price-value"})
#   print(name, price)