import random
import time

#1~45 까지의 숫자 배열 numbers 라는 배열 생성
#python make long array / make number array

#numbers 에서 숫자 6개를 비복원으로 추출
#랜덤으로 뽑은 숫자들을 lotto 변수에 담고 출력.

#추가 : lotto 변수에 담겨있는 숫자들을 오름차순으로 정렬

numbers = list(range(1,46))

#for i in range(1,45):
#    numbers.append(i)

lotto = random.sample(numbers,6)
lotto = sorted(lotto, key=int)
print(lotto)

text = ["첫 번째","두 번째","세 번째","네 번째","다섯 번째","여섯 번째"]
for i in list(range(6)):
    print("이번 주 {} 로또 추천 번호는 {} 입니다.".format(text[i],lotto[i]))
    time.sleep(2)

###############################################

#lotto = sorted(random.sample(list(range(1,46)),6))
#print(lotto)

import random
import requests
from bs4 import BeautifulSoup as bs

url = "https://m.dhlottery.co.kr/common.do?method=main"
response = requests.get(url).text
soup = bs(response,'html.parser')
document=soup.select('.prizeresult')[0]
numbers=document.select('span')

ns=[]
for number in numbers :
    ns.append(int(number.text))
print(ns)

lotto = sorted(random.sample(list(range(1,46)),6))
print(lotto)
# python check a value in a array
count = 0
for i in ns:
    if i in lotto:
        count += 1

print("해당 추천 번호 중 {}개가 지난 회차 당첨 번호에 존재합니다.".format(count))

##########

import requests
import time
from bs4 import BeautifulSoup as bs


##내가한거##
#네이버 웹툰을 가져오는 URL 파악
today = time.strftime("%a").lower()
naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
url_base = 'https://comic.naver.com'


#해당 주소로 요청을 보내 정보를 가져온다
response = requests.get(naver_url).text

#bs 이용
soup = bs(response,'html.parser')

#네이버 웹툰 페이지로 가서 원하는 정보의 위치 파악
#toons = [{"title":1,"url":2,"img_url":3}]

li = soup.select('.img_list li')
for item in li:
    title = item.select_one('dt a').text
    url = item.select('dt a')[0]['href']
    img_url = item.select('.thumb img')[0]['src']
    print(title,":", url_base+url)

"""
###toons = {
        "title" : item.select_one('dt a').text,
        "url" : item.select('dt a')[0]['href'],
        "img_url" : item.select('.thumb img')[0]['src']
    }
    print(toons)

document = soup.find_all('div', attrs={'class':'thumb'})
len(document)
#print(document)
for i in range(3,len(document)):
    title = document[i].find('a').get('title')
    url_part = document[i].find('a').get('href')
    url_final = url_base + url_part
    print(title,":", url_final)

#오늘자 업데이트된 웹툰들의 각각 리스트 페이지, 웹툰의 제목
#저장한 문서를 이용해 원하는 정보의 위치를 뽑아낸다
#출력한다
"""