# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk
# nltk 모듈에서 Stopwords를 직접 불러온다
from nltk.corpus import stopwords

# nltk의 WordNetLemmatizer를 불러와 lemmatizer 변수에 저장한다
lemmatizer = nltk.wordnet.WordNetLemmatizer()
# 영어의 stopwords를 불러와 변수에 저장한다
stopWords = stopwords.words('english')

# open 함수를 통해 'result-1-3-4.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-4.txt', 'r', encoding = 'utf-8') as f: 		# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()											# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()														# 파일을 닫는다														

firstReview = lines[0]												# 첫 번째 리뷰를 가져와 변수에 저장한다
tokens = nltk.word_tokenize(firstReview)							# 첫 번째 리뷰를 tokenize한다
lemmas = []															# lemmatize한 결과를 담기 위한 리스트를 생성한다

# for문을 통해 stopwords 제거와 lemmatization을 수행한다
for token in tokens:												
	if token.lower() not in stopWords:								# 소문자로 변환한 token이 stopwords에 없으면:
		lemmas.append(lemmatizer.lemmatize(token))					# lemmatize한 결과를 리스트에 첨부한다

print('Lemmas of the first review: ')								# lemmatize한 결과를 출력한다
print(lemmas)