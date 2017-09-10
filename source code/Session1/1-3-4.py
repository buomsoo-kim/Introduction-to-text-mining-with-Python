# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 시작 URL을 입력한다
baseURL = 'http://www.imdb.com/title/tt0468569/reviews?start='

# urlopen 함수를 통해 web 변수를 생성('0'을 더해 첫 번째 리뷰부터 시작함을 알려준다)
web = urlopen(baseURL + '0')

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
source = BeautifulSoup(web, 'html.parser')

# 리뷰 데이터가 있는 테이블을 찾는다
table = source.find('div', {'id': 'tn15content'})

page_no = 10                    # 출력하고자 하는 총 페이지 개수를 입력
reviewList = []                 # 리뷰 내용을 담고자 하는 리스트를 생성
status = True                   # while문을 탈출하기 위한 조건을 설정하는 status 변수 생성
i = 0                           # 현재 크롤링한 리뷰 수를 기록하기 위한 i 변수 생성

# while문을 통해 10 번째 페이지까지의 리뷰를 크롤링한다
while status:
    url = baseURL + str(i)      # 시작 URL에 i를 더해 크롤링하고자 하는 페이지를 입력한다
    web = urlopen(url)          # urlopen 함수를 통해 web 변수를 생성 
    source = BeautifulSoup(web, 'html.parser')          # BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
    table = source.find('div', {'id': 'tn15content'})   # 리뷰 데이터가 있는 테이블을 찾는다
    
    pars = table.findAll('p')                           # 테이블 내의 모든 paragraph('p')를 찾아 리스트에 저장한다   

    # 각각의 paragraph의 내용을 저장한다
    for par in pars:
        text = par.get_text().replace('\n', ' ').replace('\r', ' ')
        # 리뷰일 경우에만 저장하기 위해 if 조건문을 활용한다
        if ('This review may contain spoilers' not in text) and ('Add another review' not in text):
            reviewList.append(text)
    i += 10                                         # 하나의 페이지를 크롤링할때마다 i를 10씩 증가시킨다
    if i >= page_no * 10:                           # 만약 현재 크롤링한 페이지 개수가 10을 넘어가면:
        status = False                              # while문을 탈출한다

# open 함수를 통해 'result-1-3-4.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-4.txt', 'w', encoding = 'utf-8') as f:        # 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다
    for review in reviewList:                                       # for문을 통해 reviewList의 각각의 리뷰를 파일에 쓴다
        f.write(review + '\n')
    f.close()                                                       # 파일을 닫는다

 