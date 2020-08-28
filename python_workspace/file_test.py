#text data file 출력
file = open("basic.txt","w")

file.write("Hello Python Programming...!\n")

file.close()

#file 입력 -> console 출력
with open("basic.txt","r") as file:
    contents=file.read()
print("입력데이터: \n",contents)

file=open("basic.txt","a")

#console 입력 -> file 출력
content=input("내용을 입력하세요 : ")
file.write(content)
file.close()

#file 입력 -> file 출력
# with open("basic.txt","r") as file:
#     contents=file.read()
# print("입력데이터: \n",contents)
read_data=open("basic.txt","r")
file=open("copybasic.txt","w")
file.write(read_data.read())
file.close()
read_data.close()