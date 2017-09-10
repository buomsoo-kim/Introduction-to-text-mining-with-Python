# 유사도 분석에 필요한 패키지를 불러온다
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 인셉션 리뷰 데이터 파일을 불러온다
with open('result-2-2-4-inception.txt', 'r', encoding = 'utf-8') as f:		# 읽기 모드('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	doc1 = ''																# 리뷰 데이터를 담기 위한 String 변수 생성				
	lines = f.readlines()													# 영화 리뷰 파일의 모든 라인을 읽어와 리스트로 저장
	for line in lines:														# for문을 통해 lines에 있는 모든 텍스트를 doc1에 이어 붙임
		doc1 += line
	f.close()																# 파일을 닫는다

# 위플래시 리뷰 데이터 파일을 불러온다
with open('result-2-2-4-whiplash.txt', 'r', encoding= 'utf-8') as f:		# 읽기 모드('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	doc2 = ''																# 리뷰 데이터를 담기 위한 String 변수 생성				
	lines = f.readlines()													# 영화 리뷰 파일의 모든 라인을 읽어와 리스트로 저장
	for line in lines:														# for문을 통해 lines에 있는 모든 텍스트를 doc2에 이어 붙임
		doc2 += line
	f.close()																# 파일을 닫는다

corpus = [doc1, doc2]														# doc1, doc2를 합쳐 corpus list를 생성
vectorizer = TfidfVectorizer()												# TfidfVectorizer() 변수 생성
X = (vectorizer.fit_transform(corpus)).todense()							# fit_transform()를 통해 corpus의 텍스트 데이터를 벡터화해 X에 저장하고 
																			# X를 dense한 matrix로 변환

# 인셉션과 위플래시 간의 cosine similarity 계산
print("Similarity between 'Inception' and 'Whiplash': ", cosine_similarity(X[0], X[1]))
