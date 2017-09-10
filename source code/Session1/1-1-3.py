# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 검색하고 싶은 단어 입력하기
words = ['curiosity', 'killed', 'the', 'cat']					# 단어를 여러 개 검색할 것이므로 복수의 단어를 리스트에 저장한다

# open 함수를 통해 'result-1-1-3.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-1-3.txt', 'w', encoding = 'utf-8') as f:	# 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다
	for word in words:											# for문을 통해 각각의 단어와 그 뜻을 저장한다
		url = 'http://dic.daum.net/search.do?q=' + word 		# 불러오려는 url 입력하기 
		web = urlopen(url)										# urlopen 함수를 통해 web 변수를 생성	
		web_page = BeautifulSoup(web, 'html.parser')			# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
		# find 함수를 통해 찾고자 하는 단어와 단어의 뜻이 있는 HTML 태그를 찾음
		box = web_page.find('div', {'class': 'search_cleanword'}).find('span',{'class': 'txt_emph1'})	# 단어가 있는 곳
		box2 = web_page.find('ul', {'class': 'list_search'})											# 단어의 뜻이 있는 곳
		# get_text 함수로 텍스트를 추출하고 이를 저장한다
		# write 함수로 파일에 내용을 쓴다
		f.write(box.get_text() + '\n')				
		f.write(box2.get_text() + '\n')
	f.close()													# 파일을 닫는다