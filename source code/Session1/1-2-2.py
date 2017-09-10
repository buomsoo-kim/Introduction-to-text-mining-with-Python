# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 불러오려는 url 입력하기 - 코인마켓캡 닷컴
url = 'https://coinmarketcap.com/'

# urlopen 함수를 통해 web 변수를 생성
web = urlopen(url)

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
web_page = BeautifulSoup(web, 'html.parser')

# 코인과 관련된 데이터가 있는 곳을 찾는다
table = web_page.find('table', {'id': 'currencies'})							# 1위부터 100위까지의 cryptocurrency 데이터가 있는 테이블을 찾는다
coinNames = table.findAll('td', {'class': 'no-wrap currency-name'})				# 코인의 이름(name)이 있는 곳들을 찾아 리스트로 저장한다
marketCaps = table.findAll('td', {'class': 'no-wrap market-cap text-right'})	# 코인의 시가총액(market cap)이 있는 곳들을 찾아 리스트로 저장한다
prices = table.findAll('a', {'class': 'price'})									# 코인의 가격(price)이 있는 곳들을 찾아 리스트로 저장한다
volumes = table.findAll('a', {'class': 'volume'})								# 코인의 24시간 볼륨(volume)이 있는 곳들을 찾아 리스트로 저장한다

# open 함수를 통해 'result-1-2-2.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-2-2.txt', 'w', encoding = 'utf-8') as f:					# 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다
	# for문을 통해 시가총액 1위부터 100위까지의 코인의 정보를 저장한다
	for i in range(100):														# 리스트 인덱스 접근을 위해 0부터 100까지 iterate 한다
		# 하나의 코인에 대한 정보를 row에 입력한다
		# 중간중간에 '\t'를 입력하여 각각의 데이터를 구분한다
		row = coinNames[i].get_text().strip() + '\t' + marketCaps[i].get_text().strip() + '\t' \
			+ prices[i].get_text().strip() + '\t' + volumes[i].get_text().strip() + '\n'
		f.write(row)															# row를 파일에 쓴다
	f.close()																	# 파일을 닫는다