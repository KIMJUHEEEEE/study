class AIEntity:
    #생성자정의 : member variation - name, age, email, major 초기화
    def __init__(self,name,age,email,major):
        self.name=name
        self.email=email
        self.age=age
        self.major=major
   
    #email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self,email):
        if(self.email==email):
            return True
        else:
            return False
    def __str__(self):
        return "{0} : {1} : {2} ".format(self.name,self.email,self.major)


    