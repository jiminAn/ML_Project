## SGDClassifier란?

------

- SGD(Stochastic Gradient Descent)를 이용한 정규화된 선형 분류 모델
- 계산값을 기반으로 계산값이 0보다 작으면 -1, 0보다 크면 1로 분류한다
- 이진 선형 분류기는 선, 평면, 초평면을 이용해 2개의 클래스를 구분하는 분류기이다

###  

### SGD(Stochastic Gradient Descent)란?

NN(Neural Network)의 가중치(Weight)를 조정하는 과정에서 보통 경사하강법(Gradient Descent)을 사용한다. 이는 네트워크의 파라미터를 p라고 했을 때, 네트워크에서 내놓는 결과값과 실제 값 사이의 차이를 정의하는 손실 함수(loss function, 혹은 비용함수(cost fuction))의 값을 최소화하기 위해 기울기를 이용하는 것이다. 경사하강법에는 손실 함수의 값을 최소화하는 p를 찾는 것으로 기울기의 반대 방향으로 일정 크기만큼 이동하는 것을 반복한다. 

![img](https://blog.kakaocdn.net/dn/eeSIEz/btrgWDVDXkv/70SbjZsXK5MSrCwi6P4EnK/img.png)손실함수를 이용한 경사 하강법 그래프 : 지역최소값과 전역최소값 

SGD에서는 손실 함수를 계산할 때, 전체 데이터(Batch) 대신 일부 데이터의 모음(Mini-Batch)를 사용하여 계산한다. 기존의 전체 학습 데이터 셋을 이용하는 배치 경사 하강법보다 다소 부정확할 수는 있지만, 계산 속도가 훨씬 빠르기 때문에 같은 시간에 더 많은 스텝을 갈 수 있으며, 여러 번 반복할 경우 배치로 처리한 결과고 수렴한다. 또한 배치 경사 하강법의 단점인 지역 최소값(Local Minima)에 빠지지 않고 전역 최소값(Global Minima)에 수렴할 가능성이 높다. 



### SGDClassifier을 사용하는 이유

- SGD는 미니배치를 사용하여 학습하기 때문에, 배치 경사 하강법보다 큰 데이터를 학습 시킬 때 효과적이다.
- 선형회귀(Logistic Regression)의 손실 함수 최소값은 직접적으로 계산할 수 없지만, SGD를 통해서는 최소값을 직접 계산할 수 있다 이 과정에서 손실함수를 최소값 가까이로 조정할 수 있다.
- 램(RAM)에 계속 기록을 저장하지 않으면 수행할 수 없는 SVM(Support Vector Machine)이나 선형회귀와 다르게 계속해서 수행 할 수 있다

##  



## Scikit-Learn Library : SGDClassifier 사용법

------

```
SGDClassifier(alpha, average, class_weight, epsilon, eta0, fit_intercept, l1_ratio, 
	      learning_rat, loss, max_iter, n_iter, n_jobs, penalty, power_t, 
              random_state, shuffle, tol, verbose, warm_start)
```

- 확률적 경사하강법(SGD, Stochastic Gradient Descent)을 이용하여 선형모델을 구현
- loss : 손실함수 (default='hinge', which gives a linear SVM)
  - possible option : hinge, log, modified_huber, squared_hinge, perceptron, squared_error, huber, eplsilon_insensitive, squared_epsilion_insensitive
    - log : logistic regression, a probabilistic classifer
    - modified_huber : smooth loss that brings tolerance to outliers as well as probability estimates
    - squared_hinge : like hinge, but is quadratically penalized
    - perceptron : lineal loss used by the perceptron algorithm
- penalty : {'l2', 'l1', 'elasticnet'}, default='l2'
  - l2 : standard reqularizer for linear SVM models
  - l1 , elasticnet : bring sparsity to the model(feature selection) not achievable with 'l2'
- alpha : 값이 클수록 강력한 정규화(규제) 설정 (default=0.0001)
  - Also, used to compute the learning rate when set to 'learning_rate' is set to optimal
- l1_ratio : L1 규제의 비율(Elastic-Net 믹싱 파라미터 경우에만 사용) (default=0.15)
- fit_intercept : 모형에 상수항(절편)이 있는가 없는가를 결정하는 인수 (default=True)
- max_iter : 계산에 사용할 작업 수 (default=1000)
  - only impacts the behavior in the 'fit' method, and not the 'partial_fit' method
- tol : 정밀도(None이 아닐 경우, 학습은 loss > best_loss- tol 일 때 중지된다)
  - Convergence is checked against the training loss or the validation loss depending on the 'early_stopping' prarameter
- shuffle : 각 에포크 후에 트레이닝 데이터를 섞는 유무 (default=True)
- verbose : verbosity level 설정 ,int (default = 0)
- epsilon : 손실 함수에서의 엡실론, 엡실론이 작은 경우, 현재 예측과 올바른 레이블 간의 차이가 임계 값보다 작으면 무시 (default=0.1)
- n_jobs : 병렬 처리 할 때 사용되는 CPU 코어 수
- random_state : 난수 seed 설정
- learning_rate : 학습속도 (default='optimal')
  - the learning rate schedule
    - 'const' : eta = eta0
    - 'optimal' : eat = 1.0 / (alpha * (t + t0))
    - 'invscaling' : eta = eat0 / pow(t, power_t)
    - 'adaptive' : eta = eat0
- eta0 : 초기 학습속도 (default=0.0)
- power_t : 역 스케일링 학습률 (default=0.5)
- early_stopping : 유효성 검사 점수가 향상되지 않을 때 조기 중지여부 (default=False)
- validation_fraction : 조기 중지를위한 검증 세트로 설정할 교육 데이터의 비율 (default=0.1)
- n_iter_no_change : 조기중지 전 반복횟수 (default=5)
- class_weight : 클래스와 관련된 가중치 {class_label: weight} or “balanced”, default=None
- warm_start : 초기화 유무 (default=False)
- average : True로 설정하면 모든 업데이트에 대한 평균 SGD 가중치를 계산하고 결과를 coef_속성에 저장 (default=False)
