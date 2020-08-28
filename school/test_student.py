import student_class

ai_list=[student_class.Student("ai01","김주희","전자공학"),student_class.Teacher("ai01","aaa","파이썬"),student_class.Employee("e01","bbb","교육")]

if ai_list[0]==ai_list[1]:
    print("존재하는 데이터")
else:
    print("등록가능한 데이터")

# ai01=student_class.Student("ai01","김주희","전자공학")
# ai01.student_info()

# t01=student_class.Teacher("T01","aaa","파이썬")
# t01.teacher_info()

# e01=student_class.Employee("e01","bbb","교육")
# e01.employee_info()

for ai in ai_list:
    ai.info()
    # if isinstance(ai,student_class.Student):
    #     ai.student_info()
    # elif isinstance(ai,student_class.Teacher):
    #     ai.teacher_info()
    # elif isinstance(ai,student_class.Employee):
    #     ai.employee_info()
    # else:
    #     print("타입이 잘못됐습니다.")

