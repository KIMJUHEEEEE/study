def store(AI_list):
    data_write=open("student_list.txt","w")
    for index, value in enumerate (AI_list):
        data_write.write("{0}번째 정보 : {1}\n".format(index+1,value))

def init(AI_list):
    data_read=open("student_list.txt","r")
    for line in data_read:
        b=line.strip().split("'")
        L={"name":b[3],"age":b[7],"major":b[11]}
        AI_list.append(L)
    data_read.close()