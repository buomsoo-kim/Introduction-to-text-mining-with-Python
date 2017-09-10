# 텍스트 분석을 위해 nltk 모듈을 불러온다
import nltk

# nltk의 WordNetLemmatizer를 불러와 lemmatizer 변수에 저장한다
lemmatizer = nltk.wordnet.WordNetLemmatizer()

# 전처리하고자 하는 문장을 String 변수로 저장한다
sent1 = 'My only regret in life is that I did not drink more wine.'
sent2 = 'I drink to make other people more interesting.'
sent3 = 'An intelligent man is sometimes forced to be drunk to spend time with his fools.'

## 문장1 lemmatize하기:
print('Lemmatizing Sentence 1:')
lemma1 = []											# lemmatize된 token들을 담기 위한 리스트를 생성한다
tokens1 = nltk.word_tokenize(sent1)					# 문장을 tokenize한다
for token in tokens1:								# for문을 통해 각각의 token을 lemmatize한다
	lemma1.append(lemmatizer.lemmatize(token))
print(lemma1)										# lemmatize된 결과를 출력한다

## 문장2 lemmatize하기:
print('Lemmatizing Sentence 2:')
lemma2 = []											# lemmatize된 token들을 담기 위한 리스트를 생성한다
tokens2 = nltk.word_tokenize(sent2)					# 문장을 tokenize한다
for token in tokens2:								# for문을 통해 각각의 token을 lemmatize한다
	lemma2.append(lemmatizer.lemmatize(token))
print(lemma2)										# lemmatize된 결과를 출력한다

## 문장3 lemmatize하기:
print('Lemmatizing Sentence 3:')
lemma3 = []											# lemmatize된 token들을 담기 위한 리스트를 생성한다
tokens3 = nltk.word_tokenize(sent3)					# 문장을 tokenize한다
for token in tokens3:								# for문을 통해 각각의 token을 lemmatize한다
	lemma3.append(lemmatizer.lemmatize(token))
print(lemma3)										# lemmatize된 결과를 출력한다
