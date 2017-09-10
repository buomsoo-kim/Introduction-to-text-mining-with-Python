# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk
# nltk 모듈에서 Stopwords를 직접 불러온다
from nltk.corpus import stopwords

# 영어의 stopwords를 불러와 변수에 저장한다
stopWords = stopwords.words('english')

# 전처리하고자 하는 문장을 String 변수로 저장한다
sent1 = 'My only regret in life is that I did not drink more wine.'
sent2 = 'I drink to make other people more interesting.'
sent3 = 'An intelligent man is sometimes forced to be drunk to spend time with his fools.'

# 문장 1의 stopwords 제거
print('Removing stopwords in Sentence 1:')
result1 = []									# stopwords가 제거된 결과를 담기 위한 리스트를 생성한다
tokens1 = nltk.word_tokenize(sent1)				# 문장을 tokenize한다
for token in tokens1:							# for문을 통해 각각의 token이 stopwords인지 아닌지를 판별해 결과에 저장한다
	if token.lower() not in stopWords:			# 만약 소문자로 변환한 token이 stopWords 내에 없으면:
		result1.append(token)					# token을 리스트에 첨부한다
print(result1)									# 결과를 출력한다

# 문장 2의 stopwords 제거
print('Removing stopwords in Sentence 2:')
result2 = []									# stopwords가 제거된 결과를 담기 위한 리스트를 생성한다
tokens2 = nltk.word_tokenize(sent2)				# 문장을 tokenize한다
for token in tokens2:							# for문을 통해 각각의 token이 stopwords인지 아닌지를 판별해 결과에 저장한다
	if token.lower() not in stopWords:			# 만약 소문자로 변환한 token이 stopWords 내에 없으면:
		result2.append(token)					# token을 리스트에 첨부한다
print(result2)									# 결과를 출력한다

# 문장 3의 stopwords 제거
print('Removing stopwords in Sentence 3:')
result3 = []									# stopwords 제거된 결과를 담기 위한 리스트를 생성한다		
tokens3 = nltk.word_tokenize(sent3)				# 문장을 tokenize한다
for token in tokens3:							# for문을 통해 각각의 token이 stopwords인지 아닌지를 판별해 결과에 저장한다
	if token.lower() not in stopWords:			# 만약 소문자로 변환한 token이 stopWords 내에 없으면:
		result3.append(token)					# token을 리스트에 첨부한다
print(result3)									# 결과를 출력한다
