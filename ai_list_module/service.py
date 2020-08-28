from ai_exception import DuplicateException, RecordNotFoundException
#from file_store import save_data, read_data
from store import AIStore
import domain
class AIService:
    #AIEntity  정보를 저장하는 클래스 변수
    #ai_list = []
    db=AIStore()
    #수강생 등록 : email 존재여부 체크
    def register(self,ai_entity):
        result=self.is_exist(ai_entity.email)
        if not bool(result):
            AIService.db.insert(ai_entity)
            return ai_entity.name+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(ai_entity.name)
            except DuplicateException as error:
                return error

    #수강생목록
    def get_all_ai_entity(self):
        return AIService.db.select_all()

    #수강생 정보 수정
    def entity_update(self,ai_entity):
        result=self.is_exist(ai_entity.email)
        if bool(result):
            AIService.db.update(ai_entity)
            return ai_entity.name+"님 수정되었습니다."
        else:
            try:
                raise RecordNotFoundException(ai_entity.name)
            except RecordNotFoundException as removeerror:
                return str(removeerror)

    #수강생 정보 삭제
    def entity_remove(self,email):
        result=self.is_exist(email)
        if bool(result):
            AIService.db.delete(email)
            return email+"삭제되었습니다."
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeerror:
                return str(removeerror)

    #수강생 상세 정보
    def get_ai_entity(self,email):
        result=self.is_exist(email)
        if bool(result):
            ai_search=domain.AIEntity(result["name"], result["age"], result["email"], result["major"])
            return ai_search
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as searcherror:
                print(str(searcherror))
                return str(searcherror)
        # try:
        #     raise RecordNotFoundException(email)
        # except RecordNotFoundException as searchError:
        #         return str(searchError)

    #이메일 존재여부
    def is_exist(self,email):
        result=AIService.db.select_by_email(email)
        return result

    # #file store
    # def save_list(self):
    #     save_data(AIService.ai_list)

    # #file read
    # def read_list(self):
    #     AIService.ai_list=read_data()

    def close(self):
        AIService.db.close()