# data = input("정수 입력 : ")

# try:
#     print("입력받은 정수형 데이터 : {0}".format(int(data)))
# except:
#     print("정수가 아닙니다!")



#multi Exception 처리
# try:

# except ExceptionType as error:
# except ExceptionType as error2:

#자식 타입의 exception부터 처리하기!!!!

list_data=[10,20,30]
try:
    int_data=int(input("정수형 데이터 입력 : ")) #ValueError
    list_data.append(int_data)
    for index in range(len(list_data)+1): #IndexError
        #divide_sum=list_data[index]+list_data[index]/0   #ZeroDivisionError
        print("{0} 번째 데이터 : {1}".format(index,list_data[index]))
except ValueError :
    print("ValueError : 정수형 데이터를 입력하세요")
except IndexError :
    print("IndexError  : 데이터 접근은 0~{0}까지 입니다".format(len(list_data)-1))
except Exception as error:
    print(error,"프로그램에 문제가 있어 종료합니다.")