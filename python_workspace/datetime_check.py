import datetime

now=datetime.datetime.now()

#print(now.year,"년")
#print(now.month,"월")
#print(now.day,"일")
#print(now.hour,"시")
#print(now.minute,"분")
#print(now.second,"초")

m=now.month
#m=input("달을 입력하세요>>")
#m=int(m)
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31일까지 있는 달입니다.")
elif m==4 or m==6 or m==9 or m==11:
    print("30일까지 있는 달입니다.")
elif m==2:
    print("28일/ 29일까지 있는 달입니다.")
else:
    print("잘못된 값입니다.")