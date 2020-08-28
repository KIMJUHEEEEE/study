import numpy as np
import matplotlib.pyplot as plt 
import scipy.special
class Nerualnetwork:
    #신경망 초기화
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes=inputnodes
        self.hnodes=hiddennodes
        self.onodes=outputnodes

        # 가중치 행렬 wih,who
        self.wih = np.random.normal(0.0,pow(self.inodes, -0.5),(self.hnodes,self.inodes))
        self.who = np.random.normal(0.0,pow(self.hnodes, -0.5),(self.onodes,self.hnodes))
        self.lr = learningrate
        #활성화 함수 지정
        #self.activation_function = lambda x: scipy.special.expit(x)
        #activation_function(5)
        #sigmod(5) 

    def sigmoid(self,x):
        return 1/(1+(np.exp(-x)))

    #신경망 학습
    def train(self,inputs_list,targets_list):
        # 1. 입력 리스트를 2차원 행렬로 변환
        inputs = np.array(inputs_list,ndmin=2).T
        targets = np.array(targets_list, ndmin =2).T

        # 2. 은닉계층으로 들어오는 값 계산 (input-> hidden)
        hidden_inputs = np.dot(self.wih,inputs)

        # 3. 은닉계층에서 나가는 값 계산 (hidden -> output) -> sigmoid
        hidden_outputs = self.sigmoid(hidden_inputs)

        # 4. 최종계층으로 들어오는 값 계산 (hidden -> output)
        final_inputs = np.dot(self.who,hidden_outputs)

        # 5. 최종계층에서 나가는 값 계산
        final_outputs = self.sigmoid(final_inputs)

        # 6. 오차 계산 (실제 값 - 모델에 의해서 계산 된 값)
        error = targets-final_outputs

        # 7. 오차역전법 (은닉계층의 오차는 가중치에 의해 나뉜 출력 계층의 오차들의 재조합)
        hidden_errors = np.dot(self.who.T,error)

        # 8. 은닉계층과 출력계층간 가중치 업데이트
        # new w = old w - lr *(dE/do*do/dnet*dnet/dw)
        self.who += self.lr*np.array(error*final_outputs*(1-final_outputs)*hidden_outputs.T)

        # 9. 입력계층과 은닉계층간 가중치 업데이트
        self.wih += self.lr*np.array(hidden_errors*hidden_outputs*(1-hidden_outputs)*inputs.T)

    #신경망 테스트(질의)
    def test(self,inputs_list):
        # 1. 입력 리스트를 2차원 행렬로 변환
        inputs = np.array(inputs_list,ndmin=2).T

        # 2. 은닉계층으로 들어오는 값 계산
        hidden_inputs = np.dot(self.wih,inputs)

        # 3. 은식계층으로 나가는 값 계산
        hidden_outputs = self.sigmoid(hidden_inputs)

        # 4. 최종계층으로 들어오는 값 계산
        final_inputs = np.dot(self.who,hidden_outputs)

        # 5. 최종계층으로 나가는 값 계산
        final_outputs = self.sigmoid(final_inputs)

        return final_outputs


input_nodes=784
hidden_nodes=100
output_nodes=10
learning_rate=0.15

model = Nerualnetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

#학습 데이터(샘플 100) 파일 읽어오기
trainging_data_file = open('./dataset/mnist_train.csv','r')
trainging_data_list = trainging_data_file.readlines()
trainging_data_file.close()

epochs = 10
for e in range (epochs):
    for record in trainging_data_list:
        #record의 값을 [,]로 구분
        all_values = record.split(',')
        #값 조정 -> X/255.0*0.99+0.01
        inputs = (np.asfarray(all_values[1:])/255.0*0.99)+0.01
        #target 리스트 준비 (10개짜리 빈 list -> ont hot encoding)
        targets = np.zeros(output_nodes) + 0.01
        #정답을 ont hot encoding 방식으로 표시
        targets[int(all_values[0])]=0.99
        model.train(inputs,targets)
        pass

#model 검증
test_data_file = open('./dataset/mnist_test.csv','r')
test_data_list = test_data_file.readlines()
test_data_file.close()

#all_values = test_data_list[0].split(',')
# print(all_values[0])
# print(model.test((np.asfarray(all_values[1:])/255.0*0.99)+0.01))    

scorecard = []
for record in test_data_list:
    all_values = record.split(',') # 0->label, 1 ~ 입력값
    correct_label = all_values[0]
    test_list=model.test((np.asfarray(all_values[1:])/255.0*0.99)+0.01)
    print(correct_label,np.argmax(test_list))
    if np.argmax(test_list)==int(correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
print("accuracy_score=",np.asarray(scorecard).sum()/np.asarray(scorecard).size)
