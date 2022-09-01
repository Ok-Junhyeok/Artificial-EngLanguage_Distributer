# 모델가지고 취약 단어를 추출
import csv
import numpy as np

englishD=[]
labelingD=[]
with open('./voca/labelingVoca.csv') as LV:
    reader= csv.reader(LV)
    englishD=[rows for rows in reader]
for i in range(len(englishD)):
    labelingD.append(englishD[i][3])
    englishD[i].pop()
englishD=np.array(englishD)
labelingD=np.array(labelingD)

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

englishD, labelingD=load_iris(return_X_y=True)
train_input,test_input,train_target, test_target=train_test_split(englishD, labelingD, test_size=0.2,random_state=1)
gnb=GaussianNB()
y_pred = gnb.fit(train_input, train_target).predict(test_input)

'''
y_pred=gnb.fit(train_input, train_target)
a=y_pred.predict(train_input)
print(a)
'''
# 정확도
accuracy = accuracy_score(test_target, y_pred)
print("accuracy : ", accuracy)

# 예측
print(y_pred)
print("Number of mislabeled points out of a total {} points : {}".format(train_input.shape[0], (test_target!=y_pred).sum()))
# print(train_input)
# print(y_pred.predict([train_input]))

import matplotlib.pyplot as plt
plt.plot(train_input)
plt.plot(test_input)
plt.show()