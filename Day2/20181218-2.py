import requests
import time
import json
from bs4 import BeautifulSoup as bs

#1. 내가 원하는 url 담기
today = time.strftime("%a").lower()
url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+today
  
#2. 해당 url에 요청
response = requests.get(url).text

#3. python json parsing(딕셔너리 형으로 변환) 검색
#4. 파싱한다(변환한다)
document = json.loads(response)
#5. 데이터 꺼내서 조합한다
data = document['data']
toons = []

url_part = 'http://webtoon.daum.net/webtoon/view/'
for toon in data:
  title = toon['title']
  img = toon['pcThumbnailImage']['url']
  url = url_part + toon['nickname']
  print(title, ":", url)