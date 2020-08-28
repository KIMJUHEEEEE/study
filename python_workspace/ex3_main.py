import ex3_data
import ex3_view
import ex3_control
AI_list=[]
file=open("student_list.txt","a")
file.close()
ex3_data.init(AI_list)    
while True:
    x=ex3_view.view_menu()
    a=ex3_control.control(x,AI_list)
    if a==-1:
        break