# 다양한 단어의 표현 방법

## 자연어처리에서 사용하는 단어의 표현 방법

------

![image-20211013105715353](/Users/anjimin/Library/Application Support/typora-user-images/image-20211013105715353.png)

### 국소 표현(Local Representation) 

국소표현이란? 해당 단어 그 자체만 보고, 특정값을 매핑하여 단어를 표현하는 방법

국소표현의 종류

- One-hot vector
- N-gram
- Count Based
  - Bag-of-Words(DTM) : 단어의 빈도수를 카운트하여 단어를 수치화하는 표현

### 분산 표현(Continuous Representation)

분산 표현이란? 분산 표현 방법은 그 단어를 표현하고자 주변을 참고하여 단어를 표현하는 방법

분산 표현의 종류

- Prediction Based

  - Word2Vec(FastText) : 예측을 기반으로 단어의 뉘앙스를 표현

- Count based

  - Full Document
    - LSA : 단어의 뉘앙스를 반영하는 연속 표현
  - Windows
    - Glove : 예측과 카운트 두 가지 방법 모두 사용함

  

## Bag-of-Word(BoW) Model

------

기계학습 알고리즘(MLA)을 사용할 때 텍스트 그 자체로는 사용할 수 없다. 텍스트 즉, 문자열을 숫자로 바꾸어주는 과정이 필요하다

만약 문서 분류작업을 수행한다고 했을 때, 각 문서는 예측 알고리즘의 input 값에 해당하며 분류 즉, 클래스 라밸이 output값이다. 알고리즘은 input값을 숫자로 이루어진 벡터들로 받으며, 따라서 우리는 문서를 고정된 크기의 벡터로 변환하는 작업이 필요하다

기계학습을 위해 텍스트로 이루어진 문서들을 백터화하는 간단하고 효과적인 방법은 **Bag-of-Words Model(BoW)**이다

BoW는 단어들의 순서는 전혀 고려하지 않고, 단어들의 출현 빈도에만 집중하는 텍스트 데이터의 수치화 표현 방법이다.

아래와 같이 두 문장이 있을 때 Bow를 만드는 과정은 다음과 같다. 

```python
sentence1 = ["This","is","a","first","document"] 
sentence2 = ["And","this","is","a","second","document"] 
```

1. 문장안의 각 단어에 고유한 정수 인덱스를 부여한다

   ```python
   cnt = [{"This":0},{"is":1},{"a":2},{"first":3},{"document":4},
          {"And":5},{"second":6}] 
   ```

2. 각 인덱스의 위치에 단어 토큰의 등장 횟수를 기록한 벡터를 만든다

   ```python
   #index : This/is/a/first/document/And/second
   s1_Bow = [1,1,1,1,1,0,0]
   s2_Bow = [1,1,1,0,,1,1,1]
   ```

   

### CountVectorizer 

- ScikitLearn에서 제공하는 클래스로, 단어의 빈도를 Count하여 Vector로 만드는 CountVectorizer클래스로 영어에 한해서 손쉽게 BoW를 만들 수 있음

- 사용예제

  ```python
  from sklearn.feature_extraction.text import CountVectorizer
  sentence = ["This is a first document And this is a second document"]
  vector = CountVectorizer()
  
  # 문장으로부터 각 단어의 빈도수를 기록
  print(vector.fit_transform(corpus).toarray()) 
  
  # 각 단어의 인덱스가 어떻게 부여되었는지를 출력
  print(vector.vocabulary_)
  ```

  ```python
  [[2,2,1,2,1,1]]
  {"This":0,"is":1,"first":2,"document":2,"And":4,"second":5}
  ```

- 사용예제에서 확인할 수 있듯이 기본적으로 길이가 2이상인 문자에 대해서만 토큰으로 인식한다

- 단지 띄어쓰기만을 기준으로 단어를 자르는 낮은 수준의 토큰화를 진행해 Bow를 만든다

  - 단어 단위로 띄어쓰기가 명확한 영어의 경우 문제가 없다
  - 띄어쓰기가 없는 중국어, 일본어에는 적용하기 힘듦
  - 띄어쓰기가 단어 단위로 명확하지 않고, 조사 등의 이유로 한국어 역시 적응하기 힘듦



## Word2Vec Model

------

Word2Vec는 단어 간 유사도를 반영할 수 있도록 단어의 의미를 벡터화할 수 있는 방법으로 주요 아이디어는 **비슷한 분포를 가진 단어라면 비슷한 의미를 가질 것이다**이다. 즉, 자주 같이 등장할 수록 두 단어는 비슷한 의미를 가진다는 것이다. Word2Vec은 Input, Hidden, Output Layer 3개의 층으로만 이루어져 학습이 빠르고 많은 단어 뭉치를 학습할 수 있어 성능이 좋다

Word2Vec 모델은 **Continous Bag of Words(CBoW)**와 **Skip-Gram** 두 가지 방식이 있다

![image-20211013114054384](/Users/anjimin/Library/Application Support/typora-user-images/image-20211013114054384.png)



### Continous Bag of Words(CBoW)

- CBoW란? 주변에 있는 단어들을 가지고 중간에 있는 단어들을 예측하는 방법
- "The fat cat **sat** on the mat"이라는 문장이 있을 때 **sat**을 예측하는 것이 CBow이다
  - 즉 문장의 n개의 토큰이 있을 때 예측대상의 단어 인덱스는 int(n/2)이며 이를 **중심 단어(center word)**라고 한다
  - 예측에 사용되는 단어들을 **주변 단어(context word)**라고 한다
  - 중심단어를 예측하기 위해서 주변 단어의 수, 즉 앞 뒤로 몇 개의 단어를 볼지 범위를 정하게 되는데, 이 범위를 **윈도우(window)**라한다.
- 아래는 "The fat cat **sat** on the mat" 문장에서 윈도우의 크기를 2로 설정했을 때 CBoW가 학습되는 과정이다

### Skip-Gram

- Skip-Gram란? CBoW와 반대로 중간에 있는 단어로 주변 단어들을 예측하는 방법 

