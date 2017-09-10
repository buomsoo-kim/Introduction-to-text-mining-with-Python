# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 불러오려는 url 입력하기 (IMDb - 펄프 픽션)
url = 'http://www.imdb.com/title/tt0110912/?ref_=nv_sr_1'

# urlopen 함수를 통해 web 변수를 생성
web = urlopen(url)

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
web_page = BeautifulSoup(web, 'html.parser')

# 영화 제목을 출력한다
titleBar = web_page.find('div', {'class': 'titleBar'})		# 타이틀(영화 제목)이 있는 바(bar)를 찾는다
title = titleBar.find('h1', {'itemprop': 'name'})			# 타이틀바에서 영화 제목이 있는 곳을 찾는다
print('Movie: ' , title.get_text())							# get_text 함수로 영화 제목을 출력한다

# 감독 이름을 출력한다
director = web_page.find('span', {'itemprop': 'director'})	# 감독 이름이 있는 곳을 찾는다
print('Director: ', director.get_text().strip())			# get_text 함수로 감독 이름을 출력한다

# 출연 배우 이름(들)을 출력한다
table = web_page.find('table', {'class': 'cast_list'})		# 캐스팅 리스트가 있는 테이블을 찾는다
find = table.findAll('span', {'class': 'itemprop', 'itemprop': 'name'})		# 배우 이름이 있는 곳들을 찾아 리스트에 저장한다
print('Cast: ')
# for문을 통해 각 배우의 이름을 출력한다
for i in find:
	print(i.get_text())