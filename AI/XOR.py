#라이브러리 읽어오기
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

#학습 전용 데이터와 결과 준비하기
#x,y
learn_data = [[0,0],[0,1],[1,0],[1,1]]
learn_label = [0,1,1,0]


# 알고리즘 선택
clf = KNeighborsClassifier(n_neighbors=1)

#학습데이터와 정답데이터를 학습
clf.fit(learn_data,learn_label)

#검증데이터 준비
test_data=[[0,0],[0,1],[1,0],[1,1]]
test_label=clf.predict(test_data)

#예측 결과 평가하기
print(test_data,"의 예측 결과: ",test_label)
print("정답률 = ",accuracy_score([0,1,1,0],test_label))