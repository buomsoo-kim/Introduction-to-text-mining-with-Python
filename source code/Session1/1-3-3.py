# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 불러오려는 url 입력하기
url = 'http://www.imdb.com/title/tt0468569/reviews?start=0'

# urlopen 함수를 통해 web 변수를 생성
web = urlopen(url)

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
source = BeautifulSoup(web, 'html.parser')

# 리뷰 데이터가 있는 테이블을 찾는다
table = source.find("div", {"id": "tn15content"})

# 테이블 내의 모든 paragraph('p')를 찾아 리스트에 저장한다
pars = table.findAll('p')

# 각각의 paragraph의 내용을 출력한다
for par in pars:
	# 리뷰일 경우에만 출력하기 위해 if 조건문을 활용한다
    if ('This review may contain spoilers' not in par) and ('Add another review' not in par):
        print(par.get_text().replace('\n', ' ').replace('\r', ' '))
        break
