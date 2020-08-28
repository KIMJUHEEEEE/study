class MemberEntity:
    def __init__(self,email,MemberName,PhoneNumber,BirthDay,address,password):
        self.email=email
        self.MemberName=MemberName
        self.PhoneNumber=PhoneNumber
        self.BirthDay=BirthDay
        self.address=address
        self.password=password


class ClubEntity:
    def __init__(self,ClubName,intro,leader,FoundationDay):
        self.ClubName=ClubName
        self.intro=intro
        self.leader=leader
        self.FoundationDay=FoundationDay

class ClubMemberEntity:
    def __init__(self,ClubName,joinDate,email):
        self.ClubName=ClubName
        self.joinDate=joinDate
        self.email=email

class BoardEntity:
    def __init__(self,ClubName,BoardName,BoardNumber,admin):
        self.ClubName=ClubName
        self.BoardName=BoardName
        self.BoardNumber=BoardNumber
        self.admin=admin

class PostEntity:
    def __init__(self,ClubName,BoardName,PostName,writer,contents):
        self.ClubName=ClubName
        self.BoardName=BoardName
        self.PostName=PostName
        self.writer=writer
        self.contents=contents


