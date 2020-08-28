AI_list=[]
def register(AI_list):
    n=input("이름을 입력하세요 :")
    a=input("나이를 입력하세요 :")
    m=input("전공을 입력하세요 :")
    L={"name":n,"age":a,"major":m}
    AI_list.append(L)
    return "등록되었습니다."

def ai_list():
     print(AI_list)


def ai_remove(name):
    id=ai_search(name)
    if id==-1:
        print("수강생 정보가 없습니다.")
        return
    del AI_list[id]
    print("삭제 성공!")

def ai_update(AI_list):
    a=input("수정할 수강생 이름을 입력하세요")
    id=ai_search(a)
    if id==-1:
        print("수강생 정보가 없습니다.")
        return
    n=input("수정할 이름을 입력하세요 ")
    a=input("수정할 나이를 입력하세요 :")
    m=input("수정할 전공을 입력하세요 :")
    AI_list[id]["name"]=n
    AI_list[id]["age"]=a
    AI_list[id]["major"]=m
    print("수정 성공!")

def ai_search(name):
    id=-1
    for i in range(len(AI_list)):
        if name==AI_list[i]["name"]:
            id=i
            break
    return id

def ai_exist(name):
    i=ai_search(name)
    if i!=-1:
        print("수강생 이름이 있습니다.")
    else:
        print("수강생 이름이 없습니다.")

            

while True:
    x=input("---메뉴를 입력하세요---\n 1: AI 수강생 등록\n 2: AI 수강생 목록\n 3: AI 수강생 삭제\n 4: AI 수강생 수정\n 5: AI 수강생 이름 검색\n 0: 종료\n")
    if x=='1':
        register(AI_list)
    elif x=='2':
        ai_list()
    elif x=='3':
        print(AI_list)
        a=input("삭제할 이름을 입력하세요 : ")
        ai_remove(a)
    elif x=='4':
        print(AI_list)
        ai_update(AI_list)
    elif x=='5':
        n=input("수강생 이름을 검색합니다.")
        ai_exist(n)
    elif x=='0':
        print("종료합니다")
        break