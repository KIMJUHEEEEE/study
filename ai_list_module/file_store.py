import os.path
import domain
#파일 저장
def save_data(ai_list):
    data_write=open("student_list.txt","w")
    for index, entity in enumerate (ai_list):
        data_write.write("{0}번째 | {1},{2},{3},{4}\n".format(index+1,entity.name,entity.age,entity.email,entity.major))

#파일 읽기
def read_data():
    ai_list=[]
    fileExist=os.path.isfile("student_list.txt")
    if fileExist:
        data_read=open("student_list.txt","r")
        for line in data_read:
            if len(line.split("|"))==2:
                ai=line.split("|")[1].rstrip("\n").split(",")
                ai_list.append(domain.AIEntity(ai[0].strip(),int(ai[1].strip()),ai[2].strip(),ai[3].strip()))
        data_read.close()
    return ai_list