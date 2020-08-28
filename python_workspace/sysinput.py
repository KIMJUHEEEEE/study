#string= input("인사말을 입력하세요. >")
#print(string)

#int_a=input("숫자를 입력하세요. >")
#print(int(int_a)+100) #숫자가 아닌 문자열을 변환하려하면 ValueError 발생

input_a=float(input("first > "))
input_b=float(input("second > "))

print("입력하신 데이터 {0} + {1} = {2}".format(input_a,input_b,input_a+input_b))
print("입력하신 데이터 {0} - {1} = {2}".format(input_a,input_b,input_a-input_b))
print("입력하신 데이터 {0} * {1} = {2}".format(input_a,input_b,input_a*input_b))
print("입력하신 데이터 {0} / {1} = {2}".format(input_a,input_b,input_a/input_b))
print("입력하신 데이터 {0} % {1} = {2}".format(input_a,input_b,input_a%input_b))
print("입력하신 데이터 {0} // {1} = {2}".format(input_a,input_b,input_a//input_b))