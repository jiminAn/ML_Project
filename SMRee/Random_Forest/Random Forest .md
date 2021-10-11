# Random Forest

- 다수의 결정트리들을 학습하는 앙상블 방법
- What is Decision Tree?
    - 결정 과정을 다양한 문제들로 이루어진 계층 구조로 나눈 것

## 간단하게 정리

- 설계: 서로 아주 조금씩 다른 트리들을 만들어 포레스트로 묶는다.
- 학습: 부트스트랩 방법으로 생성한 데이터셋을 1:1 매칭시켜 학습시킨다.
- 예측: 각각의 트리들이 예측한 값의 평균을 최종 예측값으로 출력한다.

## Random Forest

- 랜덤성에 의해 트리들이 아주 조금씩 다른 특성을 갖는다.
- 각 트리의 예측들이 비상관화하게 된다.
- 일반화 성능을 향상시킨다.
- 노이즈가 포함된 데이터에 대해서도 강인하게 만들어준다.
- 랜덤화는 각 트리의 훈련과정에서 진행된다.
- 랜덤화에는 주로 bagging과 랜덤 노드 최적화 방법이 사용된다.

## 장단점

- 높은 정확도
- 간단하고 빠른 학습 및 테스트
- 변수 소거 없이 많은 변수를 다룰 수 있음
- 좋은 일반화 성능
- 다중 클래스 알고리즘 특성 ?

## 중요 매개변수

T : 포레스트의 크기 (구성 트리의 개수)

- 작을 수록 훈련 시간 감소, 일반화 정도 감소
- 클 수록 훈련 시간 증가, 일반화 정도 증가

D : 최대 허용 깊이 (구성 트리의 최대 깊이)

- 클 수록 과대 적합 위험성 증가
- 작을 수록 과소 적합 위험성 증가

임의성의 정도: 각 트리들의 임의성의 정도

- |T| 인 경우 : 동일한 트리를 얻게 됨
- 1 인 경우 : 완전히 비상관화된 트리를 얻게 됨

노드 분할 함수 (각 노드가 왼쪽, 오른쪽으로 데이터를 분류하는 함수)

훈련 목적 함수

## 관련 페이지

### sklearn document

[https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### wiki

[https://ko.wikipedia.org/wiki/랜덤_포레스트](https://ko.wikipedia.org/wiki/%EB%9E%9C%EB%8D%A4_%ED%8F%AC%EB%A0%88%EC%8A%A4%ED%8A%B8)