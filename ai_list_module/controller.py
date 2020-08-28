#view에서 입력된 데이터를 체크, service의 business method 호출
# 호출된 결과값 저장, view select
from view import message_display,ai_list_display,ai_entity_display
import service
class AIController:
    
    #def __init__(self):
    #   super().__init__()

    def register_controller(self,ai_entity):
        #email valid check - regular expression 사용하여 확인
        if ai_entity.email=="" or len(ai_entity.email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
        else:
            #business method delegation
            bm = service.AIService()
            message=bm.register(ai_entity)
            #view select
            message_display(message)

    def get_all_entity_controller(self):
        bm=service.AIService()
        ai_list=bm.get_all_ai_entity()
        ai_list_display(ai_list)
        return ai_list

    def update_controller(self,ai_entity):
        if ai_entity.email=="" or len(ai_entity.email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
        else:
            #business method delegation
            bm = service.AIService()
            message=bm.entity_update(ai_entity)
            #view select
            message_display(message) 

    def delete_controller(self,email):
        if email=="" or len(email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
        else:
            #business method delegation
            bm = service.AIService()
            message=bm.entity_remove(email)
            #view select
            message_display(message) 

    def get_entity_controller(self,email):
        if email=="" or len(email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
        else:
            #business method delegation
            bm = service.AIService()
            ai_entity=bm.get_ai_entity(email)
            if ai_entity!=None:
                ai_entity_display(ai_entity)
                return ai_entity
            else:
                message_display("존재하지 않습니다.")
                return "존재하지 않습니다."

    # def file_read(self):
    #     bm=service.AIService()
    #     bm.read_list()

    def close(self):
        bm=service.AIService()
        bm.close()