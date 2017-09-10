# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# open 함수를 통해 'data-1-1-4.txt' 파일을 열고 그 내용을 가져온다
with open('data-1-1-4.txt', 'r', encoding = 'utf-8') as f:			# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'으로 설정한다
	words = f.readlines()											# readlines 함수를 통해 전체 텍스트 파일의 내용을 리스트로 가져온다 (줄로 구분)
	f.close()														# 파일을 닫는다

# open 함수를 통해 'result-1-1-4.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-1-4.txt', 'w', encoding = 'utf-8') as f:		# 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다 
	for word in words:												# for문을 통해 각각의 단어와 그 뜻을 저장한다
		url = 'http://dic.daum.net/search.do?q=' + word 			# 불러오려는 url 입력하기
		web = urlopen(url)											# urlopen 함수를 통해 web 변수를 생성	
		web_page = BeautifulSoup(web, 'html.parser')				# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
		box = web_page.find('div', {'class': 'search_cleanword'}).find('span',{'class': 'txt_emph1'})		# 단어가 있는 곳
		box2 = web_page.find('ul', {'class': 'list_search'})												# 단어의 뜻이 있는 곳
		# get_text 함수로 텍스트를 추출하고 이를 저장한다
		# write 함수로 파일에 내용을 쓴다		
		f.write(box.get_text() + '\n')
		f.write(box2.get_text() + '\n')
	f.close()														# 파일을 닫는다 