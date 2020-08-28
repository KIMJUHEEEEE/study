# CREATE TABLE member(
# 	name VARCHAR(20) NOT NULL,
# 	age int(3),
# 	email VARCHAR(50),
# 	major VARCHAR(2),
# 	PRIMARY KEY (email));
from domain import AIEntity
import pymysql.cursors
class AIStore:
    connection=None

    #db 연결
    def __init__(self):
        AIStore.connection = pymysql.connect(host='localhost',
                             port =3306,
                             user='aiadmin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        AIStore.connection.close()

    def insert(self,ai_entity):
        try:
            with AIStore.connection.cursor() as cursor:
                print(ai_entity.name)
                sql = "INSERT INTO `member` (`name`, `age`,`email`, `major`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (ai_entity.name, ai_entity.age,ai_entity.email,ai_entity.major))
                AIStore.connection.commit()
        finally:
            pass
    def select_all(self):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `member` "
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            pass
        return result

    def update(self,ai_entity):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "UPDATE member SET `name`=%s, `age`=%s,`major`=%s WHERE `email`=%s"
                cursor.execute(sql, (ai_entity.name, ai_entity.age,ai_entity.major,ai_entity.email))
                AIStore.connection.commit()
        finally:
            pass
    def delete(self,email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "DELETE FROM member WHERE `email`=%s"
                cursor.execute(sql,(email))
                AIStore.connection.commit()
        finally:
            pass
    def select_by_email(self, email):
        try:
            with AIStore.connection.cursor() as cursor:
                sql = "SELECT * FROM member WHERE `email`=%s"
                cursor.execute(sql,(email))
                result=cursor.fetchone()
        finally:
            pass
        return result

# test=AIStore()

# #test.insert(AIEntity("김주희","24","rdddffh@naver.com","전자"))
# test.update(AIEntity("김주희","23","rdddffh@naver.com","AD"))
# #result=test.seleDt_by_email("rh@naver.com")
# #test.delete("rh@naver.com")
# result=test.select_all()
# print(result)