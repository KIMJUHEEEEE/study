#메뉴 출력
def menu_display():
    print("---메뉴를 입력하세요---\n 1: AI 수강생 등록\n 2: AI 수강생 목록\n 3: AI 수강생 수정\n 4: AI 수강생 삭제\n 5: AI 수강생 이름 검색\n 0: 종료\n")

#메세지 출력
def message_display(message):
    print(message)

#수강생 목록 출력
def ai_list_display(ai_list):
    print("=== AI 수강생 목록===")
    for index,value in enumerate(ai_list):
        print("{0}번째 : {1}".format(index+1,str(value)))

#ai_entity 상세정보 출력
def ai_entity_display(ai_entity):
    print("{0} 상세정보 : {1}".format(ai_entity.email,str(ai_entity)))


#구분선
def line_display():
    print("="*30)

#ai_entity 정보입력
def input_ai_entity():
    name=input("이름을 입력하세요: ")
    age=int(input("나이를 입력하세요 :"))
    major=input("전공을 입력하세요 :")
    return name,age,major
    
#이메일 정보입력
def input_email():
    email=input("이메일을 입력하세요 : ")
    return email

# 메뉴 선택
def input_select_menu():
    menu=input("메뉴를 입력하세요 : ")
    return menu