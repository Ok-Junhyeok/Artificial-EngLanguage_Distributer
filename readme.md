# 지능형 맞춤형 그룹별 영어단어 학습
## 세부내용
 본 주제는 다음과 같은 내용을 수행하여 학습자가 자신이 영어단어 학습을 진행한 데이터로 학습데이터를 구축하고 이것을 학습한 인공지능 모델을 구축하여 본인이 취약한 단어 그룹을 분류하여 학습할 수 있는 지능형 프로그램을 제작함
 - 랜덤으로 추출된 단어 3개로 이루어진 그룹 생성
- 그룹별 단어장 생성 후 자신이 직접 그룹별 단어암기 학습 진행
- 3개다 맞춘 그룹은 1로 아닌 그룹은 0으로 레이블링하여 학습데이터 구축
- 기존 나이브베이지, 랜덤포레스트, 딥러닝 모델로 분류 모델 생성 후 학습
- 생성된 모델을 통한 취약 단어 그룹 분류 후 추천하는 프로그램 작성

## 실행
> 단어학습 <br>
`python basicEnglish.py` <br>
> 모델학습 <br>
`python Naive_Bayes.py` <br>