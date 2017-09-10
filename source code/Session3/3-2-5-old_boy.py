# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk
# nltk 모듈에서 Stopwords를 직접 불러온다
from nltk.corpus import stopwords

# 영어의 stopwords를 불러와 변수에 저장한다
stopWords = set(stopwords.words('english'))

# open 함수를 통해 'result-1-3-5-old_boy.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-5-old_boy.txt', 'r', encoding = 'utf-8') as f:		# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()													# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()																# 파일을 닫는다	

tokens = []															# token을 담기 위한 리스트를 생성한다
for line in lines:													# for문을 통해 각각의 줄에 접근한다:
	line = nltk.word_tokenize(line.lower())							# 각 라인을 소문자로 변환한 후 tokenize한다
	for word in line:												# 라인의 각 token에 for문을 통해 접근한다:
		if word not in stopWords:									# 만약 token이 stopword가 아니면:
			tokens.append(word)										# 리스트에 첨부한다

corpus = nltk.Text(tokens)											# Text() 객체를 corpus 변수에 저장한다

print(len(corpus.tokens))											# 전체 token의 개수를 출력한다
print(len(set(corpus.tokens)))										# unique한 token의 개수를 출력한다
corpus.plot(50)														# 가장 많이 등장하는 50개 단어의 빈도수를 그래프로 표현해 출력한다
print('='*50)	
print('Similar words with old boy: ')
corpus.similar('old boy')											# 'old boy'와 유사한 단어를 출력한다
print('='*50)
print('Collocations for reviews of "Old boy": ')
corpus.collocations()												# 올드 보이의 collocation을 출력한다