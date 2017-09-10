# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 검색하고 싶은 단어 입력하기
word = 'curiosity'

# 불러오려는 url 입력하기 
url = 'http://dic.daum.net/search.do?q=' + word 						# 디폴트 url에 string 타입의 word 변수를 합쳐서 url 변수 생성

# urlopen 함수를 통해 web 변수를 생성
web = urlopen(url)

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
web_page = BeautifulSoup(web, 'html.parser')

# find 함수를 통해 찾고자 하는 단어와 단어의 뜻이 있는 HTML 태그를 찾음
box = web_page.find('div', {'class': 'search_cleanword'}).find('span', {'class': 'txt_emph1'}) 	# 'curiosity' 텍스트가 있는 곳
box2 = web_page.find('ul', {'class': 'list_search'})											# 단어의 뜻이 있는 곳

# get_text 함수로 텍스트를 추출하고 이를 출력한다
print(box.get_text())																			
print(box2.get_text())