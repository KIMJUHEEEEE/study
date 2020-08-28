import ex3_data
import ex3_module
import ex3_view
def control(x,AI_list):
    if x=='1':
        ex3_module.register(AI_list)
    elif x=='2':
        ex3_view.ai_list(AI_list)
    elif x=='3':
        print(AI_list)
        a=input("삭제할 이름을 입력하세요 : ")
        ex3_module.ai_remove(a,AI_list)
    elif x=='4':
        print(AI_list)
        ex3_module.ai_update(AI_list)
    elif x=='5':
        n=input("수강생 이름을 검색합니다.")
        ex3_module.ai_exist(n,AI_list)
    elif x=='0':
        print("종료합니다")
        ex3_data.store(AI_list)
        return -1