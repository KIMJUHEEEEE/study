from store import MemberStore,ClubStore,ClubMemberStore,BoardStore,PostStore
from domain import MemberEntity,ClubEntity,ClubMemberEntity,BoardEntity,PostEntity
from exception import RecordNotFoundException, DuplicateException
class MemberService: 
    MemberDB=MemberStore()

# 멤버 중복 확인
    def is_exist_member(self,email):
        result=MemberService.MemberDB.select_Member_by_email(email)
        return result
# 이메일과 비밀번호 일치 확인
    def is_right_password(self,email,password):
        result=MemberService.MemberDB.select_Member_by_email_password(email)
        if bool(result) and result['password']==password:
            return password
        elif result==None:
            return False
        elif result['password'] != password:
            return True
   #멤버 등록
    def RegisterMember(self,MemberEntity):
        result=self.is_exist_member(MemberEntity.email)
        #pw=self.is_right_password(MemberEntity.email,MemberEntity.password)
        if not bool(result) :
            MemberService.MemberDB.insertMember(MemberEntity)
            return MemberEntity.MemberName+"님 등록되었습니다."
        else:
            try:
                raise DuplicateException(MemberEntity.MemberName)
            except DuplicateException as error:
                return error
# 멤버 수정
    def UpdateMember(self,MemberEntity):
        result=self.is_exist_member(MemberEntity.email)
        pw=self.is_right_password(MemberEntity.email,MemberEntity.password)
        if bool(result)and pw==MemberEntity.password:
            MemberService.MemberDB.updateMember(MemberEntity)
            return MemberEntity.MemberName+"님 수정되었습니다."
        elif result==None:
            try:
                raise RecordNotFoundException(MemberEntity.MemberName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        elif pw==True:
            return "비밀번호를 확인하세요."
    #멤버 삭제
    def DeleteMember(self,email,password):
        result=MemberService.MemberDB.select_Member_by_email(email)
        pw=self.is_right_password(email,password)
        if bool(result) and pw==password:
            MemberService.MemberDB.deleteMember(email)
            return email+"삭제되었습니다."
        elif result == None:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        elif pw==True:
            return "비밀번호를 확인하세요."
#멤버 목록 불러오기
    def get_all_member_entity(self):
        return MemberService.MemberDB.select_all_Member()
#검색한 멤버 상세 정보 불러오기
    def get_member_entity(self,email):
        result=MemberService.MemberDB.select_Member_by_email(email)
        if bool(result):
            #Member_search=MemberEntity(result["email"],result["MemberName"],result["PhoneNumber"],result["BirthDay"],result["address"])
            return result
        else:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as searcherror:
                return str(searcherror)
    
    def close(self):
        MemberService.MemberDB.close()

    
class ClubService:
    ClubDB=ClubStore()
#클럽 중복 확인
    def is_exist_club(self,ClubName):
        result=ClubService.ClubDB.select_Club_by_ClubName(ClubName)
        return result
#멤버 중복 확인
    def is_exist_member(self,email):
        result=MemberService.MemberDB.select_Member_by_email(email)
        return result
#비밀번호 일치 확인
    def is_right_password(self,leader,password):
        result=MemberService.MemberDB.select_Member_by_email_password(leader)
        if result['password']==password:
            return password
        else:
            return False
#클럽장 확인 
    def is_right_leader(self,ClubName,leader):
        result=ClubMemberService.ClubDB.select_Club_leader(ClubName)
        if result==leader:
            return True
        else:
            return False
#클럽 등록
    def RegisterClub(self,ClubEntity,password):
        result=self.is_exist_club(ClubEntity.ClubName)
        if bool(result):
            try:
                raise DuplicateException(ClubEntity.ClubName)
            except DuplicateException as error:
                return error
        result1=self.is_exist_member(ClubEntity.leader)
        if result1==None:
            try:
                raise RecordNotFoundException(ClubEntity.leader)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        result2=self.is_right_password(ClubEntity.leader,password)
        if not bool(result) and bool(result1) and result2==password:
            ClubService.ClubDB.insertClub(ClubEntity)
            return ClubEntity.ClubName+"클럽이 등록되었습니다."
        elif result2==False:
            return "비밀번호를 확인하세요."
#클럽 수정
    def UpdateClub(self,ClubEntity,password):
        result=self.is_exist_club(ClubEntity.ClubName)
        if result ==None:
            try:
                raise RecordNotFoundException(ClubEntity.leader)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        leader = self.is_right_leader(ClubEntity.ClubName,ClubEntity.leader)
        if leader==False:
            try:
                raise RecordNotFoundException(ClubEntity.leader)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        else:           
            pw=self.is_right_password(ClubEntity.leader,password)
            if bool(result) and pw==password:
                ClubService.ClubDB.updateClub(ClubEntity)
                return ClubEntity.ClubName+"클럽이 수정되었습니다."
            elif pw==False:
                return "비밀번호를 확인하세요."
            else:
                try:
                    raise RecordNotFoundException(ClubEntity.ClubName)
                except RecordNotFoundException as removeerror:
                    return str(removeerror)
#클럽 삭제
    def DeleteClub(self,ClubName,password):
        result=ClubService.ClubDB.select_Club_by_ClubName(ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        leader=ClubService.ClubDB.select_Club_leader(ClubName)
        pw=self.is_right_password(leader,password)
        if bool(result) and pw==password:
            ClubService.ClubDB.deleteClub(ClubName)
            return ClubName+"삭제되었습니다."
        elif pw!=password:
            return "비밀번호를 확인하세요."
#클럽 목록 불러오기
    def get_all_club_entity(self):
        return ClubService.ClubDB.select_all_Club()
#클럽 검색하기
    def get_club_entity(self,ClubName):
        result=self.is_exist_club(ClubName)
        if bool(result):
            #club_search=ClubEntity(result["ClubName"],result["intro"],result["leader"],result["FoundationDay"])
            return result
        else:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
    def close(self):
        ClubService.ClubDB.close()

class ClubMemberService(ClubService):
    ClubMemberDB=ClubMemberStore()
    ClubDB=ClubStore()
#클럽 존재 확인
    def is_exist_club(self,ClubName):
        result=ClubService.ClubDB.select_Club_by_ClubName(ClubName)
        return result
#비밀번호 확인
    def is_right_password(self,email,password):
        result=ClubService.ClubDB.select_Club_by_email_password(email)
        if result['password']==password:
            return password
        else:
            return False
#멤버 확인
    def is_exist_member(self,email):
        result=MemberService.MemberDB.select_Member_by_email(email)
        return result
  #멤버 중복 확인  
    def is_exist_club_member(self,email,ClubName):
        result = ClubMemberService.ClubMemberDB.search_Member_by_email(email,ClubName)
        return result
#클럽 멤버십 등록
    def RegisterClubMember(self,ClubMemberEntity,password):
        result=self.is_exist_club(ClubMemberEntity.ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(ClubMemberEntity.ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        else:
            result1=self.is_exist_member(ClubMemberEntity.email)
            if result1==None:
                try:
                    raise RecordNotFoundException(ClubMemberEntity.email)
                except RecordNotFoundException as removeerror:
                    return str(removeerror)
            result2=self.is_exist_club_member(ClubMemberEntity.email,ClubMemberEntity.ClubName)
            if result2!=None:
                try:
                    raise DuplicateException(ClubMemberEntity.email)
                except DuplicateException as error:
                    return str(error)
            pw=self.is_right_password(ClubMemberEntity.email,password)
            if bool(result) and bool(result1) and pw==password:
                ClubMemberService.ClubMemberDB.insertClubMember(ClubMemberEntity)
                return ClubMemberEntity.email+"님"+ClubMemberEntity.ClubName+ "클럽에 등록되었습니다."
            elif pw!=password:
                return "비밀번호를 확인하세요."


#멤버십 리스트 출력
    def GetClubMemberList(self,ClubName):
        result=self.is_exist_club(ClubName)
        if bool(result):
            return ClubMemberService.ClubMemberDB.GetClubMember(ClubName)
#멤버십 삭제
    def DeleteClubMember(self,ClubName,password,email):
        result=ClubMemberService.ClubMemberDB.search_Member_by_email(email,ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(email)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        pw=self.is_right_password(email,password)
        if result['ClubName']==ClubName and pw==password:
            ClubMemberService.ClubMemberDB.deleteClubMember(ClubName,email)
            return ClubName+"클럽 탈퇴하였습니다."
        elif pw!=password:
            return "비밀번호를 확인하세요."
        else:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)

class BoardService(MemberService):
    ClubDB=ClubStore()
    BoardDB=BoardStore()
    MemberDB=MemberService()
#클럽 존재 확인
    def is_exist_club(self,ClubName):
        result=ClubService.ClubDB.select_Club_by_ClubName(ClubName)
        return result
#게시판 중복 확인
    def is_exist_board(self,BoardName,ClubName):
        result=BoardService.BoardDB.select_board_by_boardName(BoardName,ClubName)
        return result
#비밀번호 확인
    def is_right_password(self,email,password):
        result=ClubService.ClubDB.select_Club_by_email_password(email)
        if result==None:
            return False
        if result['password']==password:
            return password
        else:
            return False
#게시판 번호 확인
    def is_exist_board_number(self,BoardNumber):
        result=BoardService.BoardDB.get_board_number(BoardNumber)
        return result
#멤버 확인
    def is_exist_member(self,email,ClubName):
        result=ClubMemberService.ClubMemberDB.search_Member_by_email(email,ClubName)
        return result
#클럽장 확인
    def is_leader(self,ClubName):
        result=ClubService.ClubDB.select_Club_leader(ClubName)
        return result
#게시판 등록
    def RegisterBoard(self,BoardEntity,password):
        result=self.is_exist_club(BoardEntity.ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(BoardEntity.ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        else:
            result1=self.is_leader(BoardEntity.ClubName)
            if result1 != BoardEntity.admin:
                return "권한이 없습니다"
            pw=self.is_right_password(BoardEntity.admin,password)
            bn=BoardService.BoardDB.get_board_max_number()
            print (bn)
            if bn['MAX(`BoardNumber`)']==None:
                BoardEntity.BoardNumber=0
            else:
                BoardEntity.BoardNumber=int(bn['MAX(`BoardNumber`)'])+1
            bd=self.is_exist_board(BoardEntity.BoardName,BoardEntity.ClubName)
            if pw==password and not bool(bd):
                BoardService.BoardDB.insertBoard(BoardEntity)
                return BoardEntity.BoardName+ "게시판이 등록되었습니다."
            elif pw != password:
                return "비밀번호를 확인하세요."
            elif bool(bd):
                try:
                    raise DuplicateException(BoardEntity.BoardName)
                except DuplicateException as error:
                    return str(error)

    #게시판 수정
    def UpdateBoard(self,ClubName,admin,BoardName,password,changeBoardName):
        result=self.is_exist_club(ClubName)
        resultName=self.is_exist_board(BoardName,ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        elif resultName==None:
            try:
                raise RecordNotFoundException(BoardName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        else:
            result1=self.is_leader(ClubName)
            if result1==None:
                try:
                    raise RecordNotFoundException(admin)
                except RecordNotFoundException as removeerror:
                    return str(removeerror)
            pw=MemberService.MemberDB.select_Member_by_email_password(result1)
            print(pw)
            if pw==None or pw['password']!=password:
                return "비밀번호를 확인하세요."
            elif result1==admin and pw['password']==password:
                BoardService.BoardDB.updateBoard(BoardName,changeBoardName,ClubName)
                return BoardName+"수정되었습니다."
            elif result1!=admin:
                    return "권한이 없습니다."
#게시판 삭제
    def DeleteBoard(self,ClubName,BoardName,password,admin):
        result2=self.is_exist_club(ClubName)
        if result2==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
        result=self.is_exist_board(BoardName,ClubName)
        result1=self.is_leader(ClubName)
        pw=MemberService.MemberDB.select_Member_by_email_password(result1)
        if bool(result) and bool(result1) and pw['password']==password:
            BoardService.BoardDB.deleteBoard(BoardName,ClubName)
            return BoardName+"삭제되었습니다."
        elif result1!=admin:
            return "권한이 없습니다."
        elif pw['password']!=password:
            return "비밀번호를 확인하세요."
        else:
            try:
                raise RecordNotFoundException(BoardName)
            except RecordNotFoundException as removeerror:
                return str(removeerror)
#게시판 목록 불러오기
    def GetBoardList(self,ClubName,member,password):
        result1=self.is_exist_member(member,ClubName)
        result3=self.is_exist_club(ClubName)
        pw=self.is_right_password(member,password)
        if result3==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return ClubName+str(removeerror) 
        elif result1 ==None:
            try:
                raise RecordNotFoundException(member)
            except RecordNotFoundException as removeerror:
                return member+str(removeerror)     
        elif bool(result1) and bool(result3) and pw==password:
            return BoardService.BoardDB.get_all_Board(ClubName)       
        elif pw !=password:
            return "비밀번호를 확인하세요."

class PostService:
    PostDB=PostStore()
    ClubDB=ClubStore()
    BoardDB=BoardStore()
    MemberDB=MemberService()
    #클럽 존재 확인
    def is_exist_club(self,ClubName):
        result=ClubService.ClubDB.select_Club_by_ClubName(ClubName)
        return result
#게시판 존재 확인
    def is_exist_board(self,BoardName,ClubName):
        result=BoardService.BoardDB.select_board_by_boardName(BoardName,ClubName)
        return result
#비밀번호 확인
    def is_right_password(self,email,password):
        result=ClubService.ClubDB.select_Club_by_email_password(email)
        if result['password']==password:
            return password
        else:
            return False
#게시글 중복 확인
    def is_exist_post(self,BoardName,PostName,ClubName):
        result=PostService.PostDB.select_Post_by_ClubName_BoardName(BoardName,ClubName,PostName)
        return result
#클럽 멤버 확인
    def is_exist_member(self,email,ClubName):
        result=ClubMemberService.ClubMemberDB.search_Member_by_email(email,ClubName)
        return result
#작성자 확인
    def is_right_writer(self,BoardName,PostName,ClubName):
        result=PostService.PostDB.select_writer(ClubName,BoardName,PostName)
        return result
#게시글 작성
    def RegisterPost(self,PostEntity,password):
        result=self.is_exist_club(PostEntity.ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(PostEntity.ClubName)
            except RecordNotFoundException as removeerror:
                return PostEntity.ClubName+str(removeerror)
        else:
            result1=self.is_exist_member(PostEntity.writer,PostEntity.ClubName)
            result2=self.is_exist_board(PostEntity.BoardName,PostEntity.ClubName)
            pw=MemberService.MemberDB.select_Member_by_email_password(PostEntity.writer)
            if bool(result1) and pw['password']==password and bool(result2):
                PostService.PostDB.insertPost(PostEntity)
                return PostEntity.PostName+ "게시글이 등록되었습니다."
            elif result1==None:
                try:
                    raise RecordNotFoundException(PostEntity.writer)
                except RecordNotFoundException as removeerror:
                    return PostEntity.writer+(removeerror)
            elif result2==None:
                try:
                    raise RecordNotFoundException(PostEntity.BoardName)
                except RecordNotFoundException as removeerror:
                    return PostEntity.BoardName+str(removeerror)                    
            elif pw!=password:
                return "비밀번호를 확인하세요."
#게시글 수정
    def UpdatePost(self,ClubName, BoardName,PostName,newPostName,newContents,password,writer):
        result=self.is_exist_club(ClubName)
        resultName=self.is_exist_board(BoardName,ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return ClubName+str(removeerror)
        elif not bool(resultName):
            try:
                raise RecordNotFoundException(BoardName)
            except RecordNotFoundException as removeerror:
                return BoardName+str(removeerror)
        else:
            result2=self.is_exist_post(BoardName,PostName,ClubName)
            if result2==None:
                try:
                    raise RecordNotFoundException(PostName)
                except RecordNotFoundException as removeerror:
                    return PostName+str(removeerror)
            result1=self.is_right_writer(BoardName,PostName,ClubName)
            print(result1)
            if result1==None:
                return "권한이 없습니다."
            if result1['writer']!=writer:
                return "권한이 없습니다."
            
            pw=MemberService.MemberDB.select_Member_by_email_password(writer)
            if result1['writer']==writer and bool(result2) and pw['password']==password:
                PostService.PostDB.updatePost(ClubName,BoardName,PostName,newPostName,newContents)
                return BoardName+"수정되었습니다."
            elif pw['password']!=password:
                return "비밀번호를 확인하세요."
#게시글 삭제
    def DeletePost(self,ClubName,BoardName,PostName,password,writer):
        result3=self.is_exist_club(ClubName)
        resultName=self.is_exist_board(BoardName,ClubName)
        if result3==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return ClubName+str(removeerror)
        elif not bool(resultName):
            try:
                raise RecordNotFoundException(BoardName)
            except RecordNotFoundException as removeerror:
                return BoardName+str(removeerror)
        else:
            result2=self.is_exist_post(BoardName,PostName,ClubName)
            if result2==None:
                try:
                    raise RecordNotFoundException(PostName)
                except RecordNotFoundException as removeerror:
                    return PostName+str(removeerror)
            result1=self.is_right_writer(BoardName,PostName,ClubName)
            if result1==None:
                return "권한이 없습니다."
            if result1['writer']!=writer:
                return "권한이 없습니다."
            pw=MemberService.MemberDB.select_Member_by_email_password(writer)
            if pw['password']!=password:
                return "비밀번호를 확인하세요."
            elif result1['writer']==writer and pw['password']==password:
                PostService.PostDB.deletePost(ClubName,BoardName,PostName)
                return PostName+"삭제되었습니다."

    #게시글 목록 불러오기
    def GetPostList(self,ClubName,BoardName,member,password):
        result3=self.is_exist_club(ClubName)
        if result3==None:
            try:
                raise RecordNotFoundException(ClubName)
            except RecordNotFoundException as removeerror:
                return ClubName+str(removeerror)  
        result=self.is_exist_board(BoardName,ClubName)
        if result==None:
            try:
                raise RecordNotFoundException(BoardName)
            except RecordNotFoundException as removeerror:
                return BoardName+str(removeerror)
        result1=self.is_exist_member(member,ClubName)
        if result1==None:
            try:
                raise RecordNotFoundException(member)
            except RecordNotFoundException as removeerror:
                return member+str(removeerror)
        pw=MemberService.MemberDB.select_Member_by_email_password(member)
        if bool(result) and bool(result1) and bool(result3) and pw['password']==password:
            return PostService.PostDB.get_all_Post(ClubName,BoardName)          
        elif pw['password']!=password:
            return "비밀번호를 확인하세요."
