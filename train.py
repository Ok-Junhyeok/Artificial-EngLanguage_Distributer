# 모델가지고 취약 단어를 추출
import csv
import numpy as np
import pandas as pd

lab=pd.read_csv('./voca/labelingVoca.csv')

# 라벨인코딩을 위해 1차원 배열로 변형
from sklearn.preprocessing import LabelEncoder
lab_input=lab[['Word1','Word2','Word3']].to_numpy()
lab_target=lab[['Label']].to_numpy()
encoder=LabelEncoder()

# 배열 복구
lab_en=encoder.fit_transform(lab_input.ravel())
lab_en=lab_en.reshape(-1, 3)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train_input,test_input,train_target, test_target=train_test_split(lab_en, lab_target, test_size=0.2,random_state=1)

from sklearn.naive_bayes import MultinomialNB

mnb=MultinomialNB()
# mnb.fit(train_input, train_target)
y_pred = mnb.fit(train_input, train_target).predict(test_input)
accuracy_train=mnb.score(train_input, train_target)
accuracy_test=mnb.score(test_input, test_target)

# 정확도
print('Accuracy-->train: {}\ntest: {}'.format(accuracy_train, accuracy_test))

# 예측
print(y_pred)
print("Number of mislabeled points out of a total {} points : {}".format(train_input[0], (test_target!=y_pred).sum()))

# 정확도
# accuracy = accuracy_score(test_target, y_pred)
# print("accuracy : ", accuracy)

# 예측
# print(y_pred)
# print("Number of mislabeled points out of a total {} points : {}".format(train_input[0], (test_target!=y_pred).sum()))
# print(train_input)
# print(y_pred.predict([train_input]))