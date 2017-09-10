# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 불러오려는 url 입력하기 - 세 개의 url이 있으므로 이를 리스트에 저장한다
urls = ['http://www.imdb.com/title/tt0110912/?ref_=nv_sr_1', \
		'http://www.imdb.com/title/tt0109830/?ref_=tt_rec_tt', \
		'http://www.imdb.com/title/tt0468569/?ref_=nv_sr_3']

info = []														# 각 영화의 정보를 담기 위한 리스트를 생성

# 각각의 url에 접속하면서 영화 정보를 가져온다
for url in urls:
	web = urlopen(url)											# urlopen 함수를 통해 web 변수를 생성
	web_page = BeautifulSoup(web, 'html.parser')				# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
	titleBar = web_page.find('div', {'class': 'titleBar'})		# 타이틀(영화 제목)이 있는 바(bar)를 찾는다
	title = titleBar.find('h1', {'itemprop': 'name'})			# 타이틀바에서 영화 제목이 있는 곳을 찾는다
	director = web_page.find('span', {'itemprop': 'director'})	# 감독 이름이 있는 곳을 찾는다

	# info 리스트에 각 영화의 정보를 저장한다
	info.append(title.get_text().strip() + '\t' + director.get_text().strip()) 

# open 함수를 통해 'result-1-3-2.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-2.txt', 'w', encoding = 'utf-8') as f:	# 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다
	# info 리스트의 각 요소의 내용을 파일에 쓴다
	for i in info:
		f.write(i + '\n')										# 각 정보는 새로운 줄('\n')으로 구분한다
	f.close()													# 파일을 닫는다