import time
#처음 메뉴 선택
def menu_display():
    print("===메뉴를 입력하세요===\n 1: 클럽 메뉴\n 2: 멤버 메뉴\n 0:종료")

#멤버 메뉴 선택
def member_menu():
    print("===메뉴를 입력하세요===\n 1:멤버 등록\n 2: 멤버 목록\n 3: 멤버 수정\n 4: 멤버 삭제\n 5: 멤버 상세 정보\n 6: 클럽 가입\n 7: 클럽 탈퇴\n a: 게시글 생성\n b: 게시글 수정\n c: 게시글 삭제\nd: 게시글 목록\n 0: 종료\n")

#클럽 메뉴 선택
def club_menu():
    print("===메뉴를 입력하세요===\n 1: 클럽 등록\n 2: 클럽 목록\n 3: 클럽 수정\n 4: 클럽 삭제\n 5: 클럽 상세 정보\n 6: 클럽 가입\n 7: 클럽 멤버 정보\n a: 게시판 생성\n b: 게시판 수정\nc: 게시판 삭제\nd: 게시판 목록\n 0: 종료\n")

#메시지 출력
def message_display(message):
    print(message)

#목록 출력
def list_display(list):
    print("=== 목록 ===")
    for index, value in enumerate(list):
        print("{0}번째 : {1}".format(index+1,str(value)))
#멤버 상세 정보 출력
def member_entity_display(member_entity):
    print("{0} 상세정보 : {1}".format(member_entity.email,str(member_entity)))

#클럽 상세 정보 출력
def club_entity_display(ClubEntity):
    print("{0} 상세정보 : {1}".format(ClubEntity.ClubName,str(ClubEntity)))   

#멤버 entity 입력
def input_member_entity():
    MemberName=input("이름을 입력하세요: ")
    PhoneNumber=input("전화번호를 입력하세요: ")
    BirthDay=input("생일을 입력하세요: ")
    address=input("주소를 입력하세요: ")
    return MemberName,PhoneNumber,BirthDay,address

#비밀번호 입력
def input_member_password():
    password=input("비밀번호를 입력하세요: ")
    return password

#이메일 입력
def input_email():
    email=input("이메일을 입력하세요: ")
    return email

#수정할 게시판 입력
def input_change_board_name():
    board_name=input("수정할 게시판 이름을 입력하세요: ")
    return board_name

#게시판 이름 입력
def input_board_name():
    board_name=input("게시판 이름을 입력하세요: ")
    return board_name

#게시판 번호 입력
def input_board_number():
    board_number=input("게시판 번호를 입력하세요: ")
    return board_number

#게시글 제목 입력
def input_post_name():
    post_name=input("게시글 제목을 입력하세요: ")
    return post_name

#게시글 내용 입력
def input_contents():
    contents=input("게시글 내용을 입력하세요: ")
    return contents

#새로운 게시글 제목 입력
def input_new_post_name():
    post_name=input("수정할 게시글 제목을 입력하세요: ")
    return post_name

#새로운 내용 입력
def input_new_contents():
    contents=input("수정할 게시글 내용을 입력하세요: ")
    return contents

#게시글 이름, 번호 입력
def input_board():
    board_name=input("게시판 이름을 입력하세요: ")
    board_number=0
    return board_name,board_number

#클럽 이름 입력
def input_ClubName():
    clubname=input("클럽 이름을 입력하세요: ")
    return clubname

#클럽 entity 입력
def input_club_entity():
    intro=input("소개를 입력하세요: ")
    leader=input("리더를 입력하세요: ")
    foundationday= time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return intro,leader,foundationday

#가입일 
def input_joinDate():
    joinDate= time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return joinDate

#메뉴 선택
def select_menu():
    menu=input("메뉴를 입력하세요: ")
    return menu


def line_display():
    print("="*30)