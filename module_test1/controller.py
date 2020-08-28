import service
from view import message_display,list_display,member_entity_display,club_entity_display
class MemberController:
    #멤버 등록
    def register_controller(self,MemberEntity):
        if MemberEntity.email=="" or len(MemberEntity.email)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.MemberService()
            message=bm.RegisterMember(MemberEntity)
            message_display(message)
            return message
    #멤버 목록 불러오기
    def get_all_Member_entity_controller(self):
        bm=service.MemberService()
        member_list=bm.get_all_member_entity()
        list_display(member_list)
        return member_list
#멤버 수정
    def update_controller(self,MemberEntity):
        if MemberEntity.email=="" or len(MemberEntity.email)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.MemberService()
            message=bm.UpdateMember(MemberEntity)
            message_display(message)
            return message
#멤버 삭제
    def delete_controller(self,email,password):
        if email=="" or len(email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            #business method delegation
            bm = service.MemberService()
            message=bm.DeleteMember(email,password)
            #view select
            message_display(message) 
            return message
#멤서 상세 정보
    def get_member_entity_controller(self,email):
        if email=="" or len(email)==0:
            #error
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            #business method delegation
            bm = service.MemberService()
            member_entity=bm.get_member_entity(email)
            if member_entity!=None:
                message_display(member_entity)
                return member_entity
            else:
                message_display("존재하지 않습니다.")
                return "존재하지 않습니다."

    def close(self):
        bm=service.MemberService()
        bm.close()


class ClubController:
    #클럽 등록
    def register_controller(self,ClubEntity,password):
        if ClubEntity.ClubName=="" or len(ClubEntity.ClubName)==0:
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            bm=service.ClubService()
            message=bm.RegisterClub(ClubEntity,password)
            message_display(message)
            return message
#클럽 목록 불러오기
    def get_all_Club_entity_controller(self):
        bm=service.ClubService()
        Club_list=bm.get_all_club_entity()
        list_display(Club_list)
        return Club_list
#클럽 수정
    def update_controller(self,ClubEntity,password):
        if ClubEntity.ClubName=="" or len(ClubEntity.ClubName)==0:
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            bm=service.ClubService()
            message=bm.UpdateClub(ClubEntity,password)
            message_display(message)
            return message
#클럽 삭제
    def delete_controller(self,ClubName,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            #business method delegation
            bm = service.ClubService()
            message=bm.DeleteClub(ClubName,password)
            #view select
            message_display(message) 
            return message
#클럽 상세정보 
    def get_club_entity_controller(self,ClubName):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            #business method delegation
            bm = service.ClubService()
            Club_entity=bm.get_club_entity(ClubName)
            if Club_entity!=None:
                message_display(Club_entity)
                return Club_entity
            else:
                message_display("존재하지 않습니다.")
                return "존재하지 않습니다."

    def close(self):
        bm=service.ClubService()
        bm.close()

class ClubMemberController:
    #멤버십 등록
    def register_controller(self,ClubMemberEntity,password):
        if ClubMemberEntity.email=="" or len(ClubMemberEntity.email)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.ClubMemberService()
            message=bm.RegisterClubMember(ClubMemberEntity,password)
            message_display(message)
            return message
#멤버십 상세 정보
    def get_entity_controller(self,ClubName):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            #business method delegation
            bm = service.ClubMemberService()
            Club_entity=bm.GetClubMemberList(ClubName)
            if Club_entity!=None:
                list_display(Club_entity)
                return Club_entity
            else:
                message_display("존재하지 않습니다.")
                return "존재하지 않습니다."
    #멤버십 탈퇴
    def delete_controller(self,ClubName,email,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        elif email=="" or len(email)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.ClubMemberService()
            message_display(bm.DeleteClubMember(ClubName,password,email))
            return bm.DeleteClubMember(ClubName,password,email)
class BoardController:
    #게시판 등록
    def register_controller(self,BoardEntity,password):
        if BoardEntity.admin=="" or len(BoardEntity.admin)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.BoardService()
            message=bm.RegisterBoard(BoardEntity,password)
            message_display(message)
            return message
#게시판 수정
    def update_controller(self,ClubName,admin,BoardName,password,change_board_name):
        if ClubName=="" or len(ClubName)==0:
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            bm=service.BoardService()
            message=bm.UpdateBoard(ClubName,admin,BoardName,password,change_board_name)
            message_display(message)
            return message

    #게시판 삭제
    def delete_controller(self,ClubName,BoardName,admin,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        elif admin=="" or len(admin)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.BoardService()
            message_display(bm.DeleteBoard(ClubName,BoardName,password,admin))
            return bm.DeleteBoard(ClubName,BoardName,password,admin)
#게시판 목록 불러오기
    def get_all_board(self,ClubName,member,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        elif member=="" or len(member)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.BoardService()
            message_display(bm.GetBoardList(ClubName,member,password))
            return bm.GetBoardList(ClubName,member,password)

class PostController:
    #게시판 등록
    def register_controller(self,PostEntity,password):
        if PostEntity.writer=="" or len(PostEntity.writer)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.PostService()
            message=bm.RegisterPost(PostEntity,password)
            message_display(message)
            return message
#게시판 수정
    def update_controller(self,ClubName,writer,BoardName,password,PostName,newPostName,newContents):
        if ClubName=="" or len(ClubName)==0:
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        else:
            bm=service.PostService()
            message=bm.UpdatePost(ClubName, BoardName,PostName,newPostName,newContents,password,writer)
            message_display(message)
            return message
#게시판 삭제
    def delete_controller(self,ClubName,BoardName,PostName,writer,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        elif writer=="" or len(writer)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.PostService()
            message_display(bm.DeletePost(ClubName,BoardName,PostName,password,writer))
            return bm.DeletePost(ClubName,BoardName,PostName,password,writer)
#게시판 목록
    def get_all_post(self,ClubName,BoardName,member,password):
        if ClubName=="" or len(ClubName)==0:
            #error
            message_display("클럽 이름 형식이 잘못되었습니다.")
            return "클럽 이름 형식이 잘못되었습니다."
        elif member=="" or len(member)==0:
            message_display("이메일 형식이 잘못되었습니다.")
            return "이메일 형식이 잘못되었습니다."
        else:
            bm=service.PostService()
            message_display(bm.GetPostList(ClubName,BoardName,member,password))
            return bm.GetPostList(ClubName,BoardName,member,password)
