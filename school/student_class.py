class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def info(self):
        print("아이디:{0}\t 이름:{1}\t".format(self.id, self.name),end="")
    def __eq__(self,id):
        if self.id==id:
            return True
        else:
            return False
            
class Student(Person):
    def __init__(self,id,name,major):
        super().__init__(id,name)
        self.major=major
    def info(self):
        super().info()
        print("전공:{0}".format(self.major))
    # def student_info(self):
    #     super().info()
    #     print("전공:{0}".format(self.major))

class Teacher(Person):
    def __init__(self, id,name,subject):
        super().__init__(id,name)
        self.subject=subject
    def info(self):
        super().info()
        print("과목:{0}".format(self.subject))
    # def teacher_info(self):
    #     super().info()
    #     print("과목:{0}".format(self.subject))

class Employee(Person):
    def __init__(self,id,name,department):
        super().__init__(id,name)
        self.department=department
    def info(self):
        super().info()
        print("부서:{0}".format(self.department))
    
    # def employee_info(self):
    #     super().info()
    #     print("부서:{0}".format(self.department))

