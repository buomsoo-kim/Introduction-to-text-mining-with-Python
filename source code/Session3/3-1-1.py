# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk
# collections 패키지로부터 Counter를 불러온다
from collections import Counter

# 명사를 담기 위한 리스트를 생성한다
nounList = []

# open 함수를 통해 'result-1-3-4.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-4.txt', 'r', encoding = 'utf-8') as f:		# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()											# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()														# 파일을 닫는다			

for line in lines:													# for문을 통해 각 줄에 접근한다:
	tokens = nltk.word_tokenize(line)								# 각 줄을 tokenize한다
	tags = nltk.pos_tag(tokens)										# tokenize한 결과를 품사 태깅한다
	for word, tag in tags:											# for 문을 통해 각각의 (단어, 태그) 쌍에 접근
		if tag in ['NN', 'NNS', 'NNP', 'NNPS']:						# 만약 태그가 명사이면:
			nounList.append(word.lower())							# 소문자로 변환한 후 리스트에 첨부한다

counts = Counter(nounList)											# 각 명사의 숫자를 센 결과를 변수에 저장한다
print(counts.most_common(10))										# 가장 흔히 등장하는 10개 명사를 출력한다