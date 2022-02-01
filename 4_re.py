import re


p = re.compile("ilra")
#.(ca.e) :하나의문자를 의미
#^ (^de) : 문자의 시작
#$(se$) : 문자의 끝
#a = "ilrara"
#m = p.match(a)
# print(m.group())
#if m:
#  print(a)
#else:
 # print("매칭되지 않음")


def print_match(m):
  if m:
    print("m.group():", m.group()) #일치하는 문자열 반환
    print("m.string:", m.string) #입력받은 문자열
    print("m.start():", m.start()) #.일치하는 문자열의 시작 index\
    print("m.end():", m.end()) #일치하는 문자여의 끝
    print("m.span():", m.span()) #일치하는 문자열의 시작 / 끝 index
  else:
    print("매칭되지 않음")
  
  
  
#m = p.search("acuilrarara")
#print_match(m)
lst = p.findall("acuilrara21 ilrara22") #일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.compile("원하는 형태")  
# 2. m = p.match("비교할 문자열") : 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환

#원하는 형태 : 정규식
#.(ca.e) :하나의 문자를 의미
#^ (^de) : 문자의 시작
#$(se$) : 문자의 끝