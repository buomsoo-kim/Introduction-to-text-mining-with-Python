# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 검색하고 싶은 단어 입력하기
words = ['curiosity', 'killed', 'the', 'cat']			# 단어를 여러 개 검색할 것이므로 복수의 단어를 리스트에 저장한다

# for문을 통해 각각의 단어와 그 뜻을 출력한다
for word in words:										# 단어의 리스트에서 각각의 단어를 꺼냄
	url = 'http://dic.daum.net/search.do?q=' + word		# 불러오려는 url 입력하기 
	web = urlopen(url)									# urlopen 함수를 통해 web 변수를 생성							
	web_page = BeautifulSoup(web, 'html.parser')		# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
	# find 함수를 통해 찾고자 하는 단어와 단어의 뜻이 있는 HTML 태그를 찾음
	box = web_page.find('div', {'class': 'search_cleanword'}).find('span',{'class': 'txt_emph1'})	# 단어가 있는 곳
	box2 = web_page.findAll('ul', {'class': 'list_search'})[0]										# 단어의 뜻이 있는 곳
	# get_text 함수로 텍스트를 추출하고 이를 출력한다
	print(box.get_text())
	print(box2.get_text())