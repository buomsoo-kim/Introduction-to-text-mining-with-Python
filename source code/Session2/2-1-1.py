# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk

# 전처리하고자 하는 문장을 String 변수로 저장한다
sent1 = 'My only regret in life is that I did not drink more wine.'
sent2 = 'I drink to make other people more interesting.'
sent3 = 'An intelligent man is sometimes forced to be drunk to spend time with his fools.'

# 각 문장을 토큰화한 결과를 출력한다
print('Tokens of Sentence 1:')
print(nltk.word_tokenize(sent1))		# 문장을 토큰화해 출력한다 
print('Tokens of Sentence 2:')
print(nltk.word_tokenize(sent2))		# 문장을 토큰화해 출력한다 
print('Tokens of Sentence 3:')
print(nltk.word_tokenize(sent3))		# 문장을 토큰화해 출력한다 
