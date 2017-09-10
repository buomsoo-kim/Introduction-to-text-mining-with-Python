# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk

# open 함수를 통해 'result-1-3-4.txt' 파일을 열고 이를 f로 지정한다
with open('result-1-3-4.txt', 'r', encoding = 'utf-8') as f:		# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()											# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()														# 파일을 닫는다

firstReview = lines[0]												# 첫 번째 리뷰를 가져와 변수에 저장한다
tokens = nltk.word_tokenize(firstReview)							# 첫 번째 리뷰를 tokenize한다
tags = nltk.pos_tag(tokens)											# tokenize한 첫 번째 리뷰를 품사 태깅 한다

print('Tokens of first review: ')									# 첫 번째 리뷰의 토큰은:
print(tokens)														# token을 출력한다
print('POS tags of first review: ')									# 첫 번째 리뷰의 POS tag는:
print(tags)															# 품사 태그를 출력한다