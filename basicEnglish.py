import random
import csv
# import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# 다항 나이브베이즈 분류기
''' 문제점
1. 단어 3개를 온전히 입력하지 않으면 labelingVoca.csv에 추가되지않으며
remove는 계속 실행되어 컴파일시 toicVoca.csv에서 뽑아낸 단어 샘플이 계속 줄어들음
2. 영어 단어랑 국어를 단순한 딕셔너리에 넣었기 때문에 다의어는 처리 불가

'''

dict_from_csv = {}

with open('./voca/toicvoca.csv', 'rt', encoding='cp949') as inp:
    reader = csv.reader(inp)
    next(reader)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

''' Initial State DICT '''
# print(dict_from_csv)


with open('./voca/labelingVoca.csv', 'at', encoding='cp949', newline='') as LV:
    wr=csv.writer(LV)
    # 랜덤 데이터 추출
    for i in range(len(dict_from_csv.keys())//3):
        print()
        A_k, B_k, C_k=list(random.sample(dict_from_csv.keys(),3)) # DeprecationWarning ---> 3.9이후 버전부터 이 코드 삭제됨

        print('A_k : {0}\nB_k : {1}\nC_k : {2}'.format(A_k, B_k, C_k))
        print()
        try:
            A_v, B_v, C_v = map(str, input().split())

            if (dict_from_csv.get(A_k)==A_v)+(dict_from_csv.get(B_k)==B_v)+(dict_from_csv.get(C_k)==C_v) >= 2:
                labelVoca=1
            else:
                labelVoca=0
        except ValueError:
            print('Be carefully to Write!')
            i-=1
        else:
            wr.writerow([A_k,B_k,C_k,labelVoca])
            # RemoveALL
            dict_from_csv.pop(A_k)
            dict_from_csv.pop(B_k)
            dict_from_csv.pop(C_k)
            A_k=str()
            B_k=str()
            C_k=str()