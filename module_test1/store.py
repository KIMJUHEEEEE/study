# create TABLE Member(
#     email varchar(30) primary key,
#     MemberName varchar(10) NOT NULL,
#     PhoneNumber varchar(20) NOT NULL,
#     BirthDay varchar(10) NOT NULL,
#     address varchar(30) NOT NULL
# );

# create TABLE CLUB(
# 	ClubName varchar(50) primary key,
# 	intro varchar(50),
# 	FoundationDay varchar(20)
# );

#create TABLE Board(
#	ClubName varchar(50) NOT NULL,
#	BoardName varchar(50) NOT NULL,
#	BoardNumber varchar(10) primary key,
#	admin varchar(10) NOT NULL);

#create TABLE Post(
#	BoardName varchar(50) NOT NULL,
#	PostName varchar(50) NOT NULL,
#	writer varchar(10),
#   contents varchar(100) NOT NULL
#	);

####미리 Member 테이블에 회원을 등록한 뒤 클럽 생성을 해야 가능합니다.###
from domain import MemberEntity, ClubEntity,ClubMemberEntity,BoardEntity,PostEntity
import pymysql.cursors
import time
class MemberStore:
    connection=None

    #db 연결
    def __init__(self):
        MemberStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


    def close(self):
        MemberStore.connection.close()
#멤버 등록
    def insertMember(self, MemberEntity):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "INSERT INTO `Members` (`email`, `MemberName`,`PhoneNumber`, `BirthDay`,`address`,`password`) VALUES (%s, %s,%s, %s, %s,%s)"
                cursor.execute(sql, (MemberEntity.email, MemberEntity.MemberName, MemberEntity.PhoneNumber,MemberEntity.BirthDay,MemberEntity.address,MemberEntity.password))
                MemberStore.connection.commit()
        finally:
            pass
#멤버 수정
    def updateMember(self, MemberEntity):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "UPDATE  `Members` SET `MemberName`=%s, `PhoneNumber`=%s,`BirthDay`=%s,`address`=%s, `password`=%s WHERE `email`=%s"
                cursor.execute(sql, (MemberEntity.MemberName, MemberEntity.PhoneNumber,MemberEntity.BirthDay,MemberEntity.address,MemberEntity.password,MemberEntity.email))
                MemberStore.connection.commit()
        finally:
            pass
#멤버 삭제
    def deleteMember(self,email):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "DELETE FROM Members WHERE `email`=%s"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
                sql = "DELETE FROM Membership WHERE `email`=%s"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
                sql = "DELETE FROM Membership WHERE `ClubName`=(SELECT ClubName FROM CLUB WHERE `leader`=%s)"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
                sql = "DELETE FROM Post WHERE `ClubName`=(SELECT ClubName FROM CLUB WHERE `leader`=%s)"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
                sql = "DELETE FROM Board WHERE `ClubName` IN (SELECT ClubName FROM CLUB WHERE `leader`=%s)"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
                sql = "DELETE FROM CLUB WHERE `leader`=%s"
                cursor.execute(sql,(email))
                MemberStore.connection.commit()
        finally:
            pass
#멤버 목록 불러오기
    def select_all_Member(self):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "SELECT email,Membername,PhoneNumber,BirthDay,address FROM `Members` "
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            pass
        return result
#멤버 상세정보 검색
    def select_Member_by_email(self, email):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "SELECT email,MemberName,PhoneNumber,BirthDay,address FROM Members WHERE `email`=%s"
                cursor.execute(sql,(email))
                result=cursor.fetchone()
        finally:
            pass
        return result
#비밀번호 일치 확인때 사용할 비밀번호 멤버 테이블에서 불러오기
    def select_Member_by_email_password(self,email):
        try:
            with MemberStore.connection.cursor() as cursor:
                sql = "SELECT password FROM Members WHERE `email`=%s"
                cursor.execute(sql,(email))
                result=cursor.fetchone()
        finally:
            pass
        return result       

class ClubStore :
    connection=None

    #db 연결
    def __init__(self):
        ClubStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


    def close(self):
        ClubStore.connection.close()
#클럽 등록
    def insertClub(self,ClubEntity):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        try:
            with ClubStore.connection.cursor() as cursor:
                print(ClubEntity.ClubName)
                sql = "INSERT INTO `CLUB` (`ClubName`, `intro`,`leader`,`FoundationDay`) VALUES (%s,%s,%s, %s)"
                cursor.execute(sql, (ClubEntity.ClubName,ClubEntity.intro,ClubEntity.leader,date))
                sql = "INSERT INTO `Membership` (`ClubName`, `joinDate`,`email`) VALUES (%s,%s,%s)"
                #date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                cursor.execute(sql, (ClubEntity.ClubName,date,ClubEntity.leader))
                ClubStore.connection.commit()
        finally:
            pass
#클럽 수정
    def updateClub(self, ClubEntity):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "UPDATE  `CLUB` SET `intro`=%s,`leader`=%s,`FoundationDay`=%s WHERE `ClubName`=%s"
                cursor.execute(sql, (ClubEntity.intro,ClubEntity.leader,ClubEntity.FoundationDay,ClubEntity.ClubName))
                ClubStore.connection.commit()
        finally:
            pass
#클럽 삭제
    def deleteClub(self,ClubName):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "DELETE FROM CLUB WHERE `ClubName`=%s"
                cursor.execute(sql,(ClubName))
                sql = "DELETE FROM Membership WHERE `ClubName`=%s"
                cursor.execute(sql,(ClubName))
                ClubStore.connection.commit()
        finally:
            pass
#클럽 정보 불러오기
    def select_Club_by_ClubName(self, ClubName):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "SELECT * FROM CLUB WHERE `ClubName`=%s"
                cursor.execute(sql,(ClubName))
                result=cursor.fetchone()
        finally:
            pass
        return result
#클럽 리더 불러오기
    def select_Club_leader(self,ClubName):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "SELECT leader FROM CLUB WHERE `ClubName`=%s"
                cursor.execute(sql,(ClubName))
                result=cursor.fetchone()
        finally:
            pass
        return result['leader']
#비밀번호 확인 위한 비밀번호 불러오기
    def select_Club_by_email_password(self,leader):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "SELECT password FROM Members WHERE `email`=%s"
                cursor.execute(sql,(leader))
                result=cursor.fetchone()
        finally:
            pass
        return result
#클럽 목록 불러오기
    def select_all_Club(self):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `CLUB` "
                cursor.execute(sql)
                result=cursor.fetchall()
                print(result)
        finally:
            pass
        return result

class ClubMemberStore:
    connection=None

    #db 연결
    def __init__(self):
        ClubMemberStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    def close(self):
        ClubStore.connection.close()
#클럽 멤버십 등록
    def insertClubMember(self,ClubMemberEntity):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        try:
            with ClubMemberStore.connection.cursor() as cursor:
                sql = "INSERT INTO `Membership` (`ClubName`, `joinDate`,`email`) VALUES (%s,%s,%s)"
                cursor.execute(sql, (ClubMemberEntity.ClubName,date,ClubMemberEntity.email))
                ClubMemberStore.connection.commit()

        finally:
            pass
#클럽 멤버십 불러오기
    def GetClubMember(self,ClubName):
        try:
            with ClubMemberStore.connection.cursor() as cursor:
                sql="SELECT ms.ClubName,ms.email, m.PhoneNumber FROM `Membership` ms, Members m WHERE `ClubName`= %s AND ms.email=m.email"
                cursor.execute(sql,ClubName)
                result=cursor.fetchall()
        finally:
            pass
        return result
#클럽 멤버 중복 확인
    def search_Member_by_email(self, email,ClubName):
        try:
            with ClubMemberStore.connection.cursor() as cursor:
                sql = "SELECT * FROM Membership WHERE `email`=%s and `ClubName`=%s"
                cursor.execute(sql,(email,ClubName))
                result=cursor.fetchone()
        finally:
            pass
        return result
#클럽 멤버 삭제
    def deleteClubMember(self,ClubName,email):
        try:
            with ClubStore.connection.cursor() as cursor:
                sql = "DELETE FROM Membership WHERE `ClubName`=%s AND `email`=%s"
                cursor.execute(sql,(ClubName,email))
                ClubStore.connection.commit()
        finally:
            pass


class BoardStore:
    connection=None

    #db 연결
    def __init__(self):
        BoardStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    def close(self):
        ClubStore.connection.close()
#게시판 중복 확인    
    def select_board_by_boardName(self,BoardName,ClubName):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "SELECT * FROM Board WHERE `BoardName`=%s AND `ClubName`=%s"
                cursor.execute(sql,(BoardName,ClubName))
                result=cursor.fetchone()
        finally:
            pass
        return result
#게시판 등록
    def insertBoard(self,BoardEntity):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "INSERT INTO `Board` (`ClubName`, `BoardName`,`BoardNumber`,`admin`) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, (BoardEntity.ClubName,BoardEntity.BoardName,BoardEntity.BoardNumber,BoardEntity.admin))
                BoardStore.connection.commit()

        finally:
            pass
#게시판 수정
    def updateBoard(self, BoardName,changeBoardName,ClubName):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "UPDATE  `Board` SET `BoardName`=%s WHERE `ClubName`=%s and `BoardName`=%s"
                cursor.execute(sql, (changeBoardName,ClubName,BoardName))
                BoardStore.connection.commit()
        finally:
            pass
#게시판 삭제
    def deleteBoard(self,BoardName,ClubName):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "DELETE FROM Board WHERE `BoardName`=%s AND `ClubName`=%s"
                cursor.execute(sql,(BoardName,ClubName))
                BoardStore.connection.commit()
        finally:
            pass
#게시판 목록
    def get_all_Board(self,ClubName):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "SELECT `BoardName` FROM Board WHERE `ClubName`=%s"
                cursor.execute(sql,(ClubName))
                BoardStore.connection.commit()
                result=cursor.fetchall()
        finally:
            pass
        return result
#게시판 번호 불러오기
    def get_board_number(self,BoardNumber):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "SELECT `BoardNumber` FROM Board WHERE `BoardNumber`=%s"
                cursor.execute(sql,(BoardNumber))
                BoardStore.connection.commit()
                result=cursor.fetchone()
        finally:
            pass
        return result
#게시판 최대번호 불러오기
    def get_board_max_number(self):
        try:
            with BoardStore.connection.cursor() as cursor:
                sql = "SELECT MAX(`BoardNumber`) FROM Board "
                cursor.execute(sql)
                BoardStore.connection.commit()
                result=cursor.fetchone()
        finally:
            pass
        return result
        


class PostStore:
    connection=None

    #db 연결
    def __init__(self):
        PostStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    def close(self):
        PostStore.connection.close()
#게시글 중복 확인
    def select_Post_by_ClubName_BoardName(self, BoardName,ClubName,PostName):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "SELECT * FROM Post WHERE `ClubName`=%s and `BoardName`=%s and `PostName`=%s"
                cursor.execute(sql,(ClubName,BoardName,PostName))
                PostStore.connection.commit()
                result=cursor.fetchone()
        finally:
            pass
        return result
#작성자 확인
    def select_writer(self,ClubName,BoardName,PostName):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "SELECT `writer` FROM Post WHERE `ClubName`=%s and `BoardName`=%s and `PostName`=%s"
                cursor.execute(sql,(ClubName,BoardName,PostName))
                PostStore.connection.commit()
                result=cursor.fetchone()
        finally:
            pass
        return result
#게시글 작성
    def insertPost(self,PostEntity):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "INSERT INTO `Post` (`ClubName`, `BoardName`,`PostName`,`writer`,`contents`) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql, (PostEntity.ClubName,PostEntity.BoardName,PostEntity.PostName,PostEntity.writer,PostEntity.contents))
                PostStore.connection.commit()

        finally:
            pass
#게시글 수정
    def updatePost(self,ClubName, BoardName,PostName,newPostName,newContents):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "UPDATE  `Post` SET `PostName`=%s, `contents`=%s WHERE `ClubName`=%s and `BoardName`=%s and `PostName`=%s"
                cursor.execute(sql, (newPostName,newContents,ClubName,BoardName,PostName))
                PostStore.connection.commit()
        finally:
            pass
#게시글 삭제
    def deletePost(self,ClubName,BoardName,PostName):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "DELETE FROM Post WHERE `PostName`=%s and `ClubName`=%s and `BoardName`=%s"
                cursor.execute(sql,(PostName,ClubName,BoardName))
                PostStore.connection.commit()
        finally:
            pass
#게시글 목록 불러오기
    def get_all_Post(self,ClubName,BoardName):
        try:
            with PostStore.connection.cursor() as cursor:
                sql = "SELECT `PostName`,`contents`,`writer` FROM Post WHERE `ClubName`=%s and `BoardName`=%s"
                cursor.execute(sql,(ClubName,BoardName))
                PostStore.connection.commit()
                result=cursor.fetchall()
        finally:
            pass
        return result
#Boardtest=BoardStore()
#ClubMembertest=ClubMemberStore()
#Posttest=PostStore()
#Membertest=MemberStore()
#Clubtest=ClubStore()
#Membertest.insertMember(MemberEntity("a@a","김주희","00000000000","971204","성남시",0000))
#Membertest.insertMember(MemberEntity("b@b","오렌지","01001010101","010101"."서울시",1111))
#Clubtest.insertClub(ClubEntity("소소한 모임","국내여행","a@a"))