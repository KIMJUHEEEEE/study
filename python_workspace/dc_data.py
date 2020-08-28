ais_1={"name":"김주희", "age":24, "major": "전자공학"}
ais_2={"name":"abc","age":25,"major":"ssss"}
ais_3={"name":"def","age":23,"major":"ffff"}
ais=[ais_1,ais_2,ais_3]
ais_3["major"]="음악"

# print("ais 정보")
# for key in ais_1:
#     print("key : {0}, value : {1}".format(key,ais_1[key]))

# print("ais 신입사원 정보")
# for ai in ais:
#     del ai["age"] # del 딕셔너리["요소"] : 삭제
#     #  print("이름 {0}, 전공 {1},이름 {2}".format(ai["name"],ai["major"],ai["age"]))  #KeyError 발생
#     print("이름 {0}, 전공 {1}".format(ai["name"],ai["major"]))

#enumerate함수 사용
# print(list(enumerate(ais)))
# for a,b in enumerate(ais):
#     print("{0} {1}".format(a,b))

#items함수 사용
print("items:", ais_1.items())
print()
for key,element in ais_1.items():
    print("dictionary[{}]={}".format(key,element))

# for i in range(len(ais)):
#     print("{0} 번째 : {1}".format(i,ais[i]))

# print()
# id=0 # 초기값 선언
# while id<len(ais):
#     print("{0} 번째 : {1}".format(id,ais[id])) # 조건값
#     id+=1 # 초기값 증감
# print()
# id=len(ais)-1# 초기값 선언
# while id>=0:
#     print("{0} 번째 : {1}".format(id,ais[id])) # 조건값
#     id-=1 # 초기값 증감

#1~10까지 짝수 출력
#for문 이용
# mlist=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(mlist)):
#     if mlist[i]%2==0:
#         print(mlist[i])
#     else:
#         continue

# print()

# #while문 이용
# id=0
# while True:
#     if id>=len(mlist):
#         break
#     if mlist[id]%2==0:
#         print(mlist[id])
#         id+=1
#     else:
#         id+=1
#         continue

#구구단 출력
#for문 이용
# for a in range(1,10):
#     for b in range(2,10):
#         print("{0} * {1} = {2}".format(b,a,a*b),end='\t')
#     print()

# print()

# #while문 이용
# x=1
# while x<10:
#     y=2
#     while y<10:
#         print("{0} * {1} = {2}".format(y,x,y*x),end='\t')
#         y+=1
#     print()
#     x+=1
