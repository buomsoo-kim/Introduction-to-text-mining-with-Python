# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk
# nltk 모듈에서 Stopwords를 직접 불러온다
from nltk.corpus import stopwords

# nltk의 WordNetLemmatizer를 불러와 lemmatizer 변수에 저장한다
lemmatizer = nltk.wordnet.WordNetLemmatizer()
# 영어의 stopwords를 불러와 변수에 저장한다
stopWords = stopwords.words('english')

# open 함수를 통해 'result-1-3-5-inception.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-5-inception.txt', 'r', encoding = 'utf-8') as f:			# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()											# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()														# 파일을 닫는다	

reviewProcessedList = []											# 처리된 결과를 담기 위한 리스트를 생성한다

# for문을 통해 각 줄을 전처리한다
for line in lines:
	reviewProcessed = ''											# 한 줄을 전처리한 결과를 담기 위한 String 변수 생성
	tokens = nltk.word_tokenize(line)								# 리뷰를 tokenize한다
	for token in tokens:
		if token.lower() not in stopWords:							# 소문자로 변환한 token이 stopwords에 없으면:
			reviewProcessed += ' ' + lemmatizer.lemmatize(token)	# lemmatize한 붙인다
	reviewProcessedList.append(reviewProcessed)						# 전처리가 끝난 리뷰를 리스트에 첨부한다

# open 함수를 통해 'result-2-2-4-inception.txt' 파일을 열고 이를 f로 지정한다
with open('result-2-2-4-inception.txt', 'w', encoding = 'utf-8') as f:			# 쓰기 형식('w')로 지정하고 인코딩은 'utf-8'로 설정한다
	for reviewProcessed in reviewProcessedList:						# 각각의 리뷰를 파일에 쓴다
		f.write(reviewProcessed + '\n')								# 각 리뷰를 줄바꿈('\n')으로 구분한다
	f.close()														# 파일을 닫는다