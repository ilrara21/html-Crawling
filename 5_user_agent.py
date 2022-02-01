import requests
url = "https://ilrara.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
res = requests.get(url, headers=headers)

res.raise_for_status()

with open("ilrara.tistory.html","w", encoding="utf-8") as f:
  f.write(res.text)