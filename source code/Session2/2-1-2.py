# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk

# 전처리하고자 하는 문장을 String 변수로 저장한다
sent1 = 'My only regret in life is that I did not drink more wine.'
sent2 = 'I drink to make other people more interesting.'
sent3 = 'An intelligent man is sometimes forced to be drunk to spend time with his fools.'

# 각 문장을 토큰화한 후 품사 태깅을 해 결과를 출력한다
print('POS tagging Sentence 1:')
tokens1 = nltk.word_tokenize(sent1)				# 문장을 토큰화한다
print(nltk.pos_tag(tokens1))					# 토큰화한 문장을 품사 태깅해 출력한다

print('POS tagging Sentence 2:')
tokens2 = nltk.word_tokenize(sent2)				# 문장을 토큰화한다
print(nltk.pos_tag(tokens2))					# 토큰화한 문장을 품사 태깅해 출력한다

print('POS tagging Sentence 3:')
tokens3 = nltk.word_tokenize(sent3)				# 문장을 토큰화한다
print(nltk.pos_tag(tokens3))					# 토큰화한 문장을 품사 태깅해 출력한다
