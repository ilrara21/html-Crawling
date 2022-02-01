

import requests
res = requests.get("https://finance.naver.com/item/main.naver?code=005930")
print("상태 :", res.status_code)

res.raise_for_status()



print(len(res.text))
print(res.text)



#with open("ssstock.html","w", encoding="utf-8") as f:
# f.write(res.text)