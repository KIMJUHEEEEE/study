import controller
import view
import domain

Mcontroller= controller.MemberController()
Ccontroller=controller.ClubController()
CMcontroller=controller.ClubMemberController()
BoardController=controller.BoardController()
PostController=controller.PostController()

while True:
    view.menu_display()
    menu=view.select_menu()
    if menu=='1':
        while True:
            view.club_menu()
            c_menu=view.select_menu()
            if c_menu=='1':
                clubname=view.input_ClubName()
                intro,leader,FoundationDay=view.input_club_entity()
                password=view.input_member_password()
                Ccontroller.register_controller(domain.ClubEntity(clubname,intro,leader,FoundationDay),password)
            elif c_menu=='2':
                Ccontroller.get_all_Club_entity_controller()
            elif c_menu=='3':
                clubname=view.input_ClubName()
                intro,leader,FoundationDay=view.input_club_entity()
                password=view.input_member_password()
                Ccontroller.update_controller(domain.ClubEntity(clubname,intro,leader,FoundationDay),password)
            elif c_menu=='4':
                clubname=view.input_ClubName()
                password=view.input_member_password()
                Ccontroller.delete_controller(clubname,password)
            elif c_menu=='5':
                clubname=view.input_ClubName()
                Ccontroller.get_club_entity_controller(clubname)
            elif c_menu=='6':
                clubname=view.input_ClubName()
                joindate=view.input_joinDate()
                email=view.input_email()
                password=view.input_member_password()
                CMcontroller.register_controller(domain.ClubMemberEntity(clubname,joindate,email),password)
            elif c_menu=='7':
                clubname=view.input_ClubName()
                CMcontroller.get_entity_controller(clubname)
            elif c_menu=='a':
                clubname=view.input_ClubName()
                admin=view.input_email()
                password=view.input_member_password()
                board_name,board_number=view.input_board()
                BoardController.register_controller(domain.BoardEntity(clubname,board_name,board_number,admin),password)
            elif c_menu=='b':
                clubname=view.input_ClubName()
                admin=view.input_email()
                password=view.input_member_password()
                board_name=view.input_board_name()
                change_board_name=view.input_change_board_name()
                BoardController.update_controller(clubname,admin,board_name,password,change_board_name)
            elif c_menu=='c':
                clubname=view.input_ClubName()
                admin=view.input_email()
                password=view.input_member_password()
                board_name=view.input_board_name()
                BoardController.delete_controller(clubname,board_name,admin,password)
            elif c_menu=='d':
                clubname=view.input_ClubName()
                member=view.input_email()
                password=view.input_member_password()
                BoardController.get_all_board(clubname,member,password)
            elif c_menu=='0':
                Ccontroller.close()
                break
            else:
                view.message_display("0부터 5까지 중에서 선택하세요")
    elif menu=='2':
        while True:
            view.member_menu()
            m_menu=view.select_menu()
            if m_menu=='1':
                email=view.input_email()
                MemberName,PhoneNumber,BirthDay,address=view.input_member_entity()
                password=view.input_member_password()
                Mcontroller.register_controller(domain.MemberEntity(email,MemberName,PhoneNumber,BirthDay,address,password))
            elif m_menu=='2':
                Mcontroller.get_all_Member_entity_controller()
            elif m_menu=='3':
                email=view.input_email()
                password=view.input_member_password()
                MemberName,PhoneNumber,BirthDay,address=view.input_member_entity()
                Mcontroller.update_controller(domain.MemberEntity(email,MemberName,PhoneNumber,BirthDay,address,password))
            elif m_menu=='4':
                email=view.input_email()
                password=view.input_member_password()
                Mcontroller.delete_controller(email,password)
            elif m_menu=='5':
                email=view.input_email()
                Mcontroller.get_member_entity_controller(email)
            elif m_menu=='6':
                clubname=view.input_ClubName()
                joindate=view.input_joinDate()
                email=view.input_email()
                password=view.input_member_password()
                CMcontroller.register_controller(domain.ClubMemberEntity(clubname,joindate,email),password)
            elif m_menu=='7':
                clubname=view.input_ClubName()
                email=view.input_email()
                password=view.input_member_password()
                CMcontroller.delete_controller(clubname,email,password)
            elif m_menu=='a':
                clubname=view.input_ClubName()
                writer=view.input_email()
                BoardName=view.input_board_name()
                password=view.input_member_password()
                postname=view.input_post_name()
                contents=view.input_contents()
                PostController.register_controller(domain.PostEntity(clubname,BoardName,postname,writer,contents),password)    
            elif m_menu=='b':
                clubname=view.input_ClubName()
                writer=view.input_email()
                BoardName=view.input_board_name()
                password=view.input_member_password()
                postname=view.input_post_name()
                newpostname=view.input_new_post_name()
                newcontents=view.input_new_contents()
                PostController.update_controller(clubname,writer,BoardName,password,postname,newpostname,newcontents)
            elif m_menu=='c':
                clubname=view.input_ClubName()
                writer=view.input_email()
                BoardName=view.input_board_name()
                password=view.input_member_password()
                postname=view.input_post_name()
                PostController.delete_controller(clubname,BoardName,postname,writer,password)
            elif m_menu=='d':
                clubname=view.input_ClubName()
                member=view.input_email()
                BoardName=view.input_board_name()
                password=view.input_member_password()
                PostController.get_all_post(clubname,BoardName,member,password)
            elif m_menu=='0':
                Mcontroller.close()
                break
            else:
                view.message_display("0부터 5까지 중에서 선택하세요")
    elif menu=='0':
        break
    else:
        view.message_display("0부터 2까지 중에서 선택하세요")
        continue