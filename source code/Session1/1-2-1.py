# 웹 크롤링에 필요한 모듈 불러오기
from bs4 import BeautifulSoup 
from urllib.request import urlopen

# 불러오려는 url 입력하기 - 코인마켓캡 닷컴
url = 'https://coinmarketcap.com/'

# urlopen 함수를 통해 web 변수를 생성
web = urlopen(url)

# BeautifulSoup으로 web 페이지상의 HTML 구조를 파싱
web_page = BeautifulSoup(web, 'html.parser')

# 비트코인과 관련된 데이터가 있는 곳을 찾아 bit 변수에 저장한다
table = web_page.find('table', {'id': 'currencies'})	# 1위부터 100위까지의 cryptocurrency 데이터가 있는 테이블을 찾는다
bit = table.find('tr', {'id': 'id-bitcoin'})			# 비트코인 데이터가 행(첫째 행)의 데이터를 찾는다

# 비트코인 관련된 데이터를 출력한다
coinName = bit.find('td', {'class': 'no-wrap currency-name'})			
print('Coin Name: ', coinName.get_text().strip())							# 코인의 이름('Bitcoin')을 출력한다
marketCap = bit.find('td', {'class': 'no-wrap market-cap text-right'})
print('Market Cap: ', marketCap.get_text().strip())							# 코인의 시가총액(Market cap)을 출력한다
price = bit.find('a', {'class': 'price'})									
print('Price: ', price.get_text().strip())									# 코인의 가격(price)를 출력한다
volume = bit.find('a', {'class': 'volume'})
print('Volume: ', volume.get_text().strip())								# 코인의 24시간 볼륨(volume)을 출력한다

