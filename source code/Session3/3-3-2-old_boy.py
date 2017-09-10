## 분석을 위해 필요한 모듈을 불러온다
import nltk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# unique한 명사를 저장하기 위한 셋을 생성한다
unqiueNouns = set()
# 문장을 담기 위한 리스트를 생성한다
sentences = []

# open 함수를 통해 'result-2-2-4-old_boy.txt' 파일을 열고 이를 f로 지정한다
with open('result-2-2-4-old_boy.txt', 'r', encoding = 'utf-8') as f:		# 읽기 형식('r')로 지정하고 인코딩은 'utf-8'로 설정한다
	lines = f.readlines()													# readlines 함수로 텍스트 파일의 내용을 읽어 리스트로 저장한다
	f.close()																# 파일을 닫는다		

for line in lines:													# for문을 통해 각 줄에 접근한다:
	tokens = nltk.word_tokenize(line)								# 각 줄을 tokenize한다
	tags = nltk.pos_tag(tokens)										# tokenize한 결과를 품사 태깅한다
	sentences.append(tags)											# 태그를 리스트에 첨부한다

	for word, tag in tags:											# tags의 (단어, 태그)쌍을 하나씩 꺼낸다:
		if tag in ['NN', 'NNS', 'NNP', 'NNPS']:						# 만약 태그가 명사면:
			unqiueNouns.add(word)									# 셋에 명사를 첨부한다

unqiueNouns = list(unqiueNouns)										# uniqueNouns 셋을 리스트로 변환한다
nounIndex = {noun: i for i, noun in enumerate(unqiueNouns)}			# enumerate 함수로 각 명사의 index를 지정한다

matrix = np.zeros([len(sentences), len(unqiueNouns)])				# [(문장의 개수) X (unique한 명사의 개수)]크기의 0으로 이루어진 행렬을 생성한다

for i, sentence in enumerate(sentences):							# enumerate 함수로 각 sentence의 index를 지정한다
	for word, tag in sentence:										# 각 문장의 token들의 (word, tag) 쌍에서:
		if tag in ['NN', 'NNS', 'NNP', 'NNPS']:						# 만약 태그가 명사면:
			index = nounIndex[word]									
			matrix[i][index] = 1									# 행렬의 [i],[index] 번째 원소를 1로 설정한다

coocurMatrix = matrix.T.dot(matrix)									# 행렬의 내적 연산을 통해 co-occurence matrix를 계산한다

graph = nx.Graph()													# 그래프를 생성한다

## co-occurence matrix의 값들로 그래프를 그려간다
for i in range(len(unqiueNouns)):
	for j in range(i+1, len(unqiueNouns)):
		if coocurMatrix[i][j] > 30:
			graph.add_edge(unqiueNouns[i], unqiueNouns[j])

# 그래프를 시각화한다
plt.figure(figsize=(15, 15))										# 사이즈는 (15,15)로 설정한다
layout = nx.random_layout(graph)									# random_layout을 적용한다
nx.draw(graph, pos=layout, with_labels=True,						# 그래프를 그린다
        font_size=20, alpha=0.3, node_size=3000)
plt.show()															# 그래프를 화면에 띄운다