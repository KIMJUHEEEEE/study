from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import controller
import view
import domain

Mcontroller= controller.MemberController()
Ccontroller=controller.ClubController()
CMcontroller=controller.ClubMemberController()
BoardController=controller.BoardController()
PostController = controller.PostController()

#제일 처음 화면 - 클럽 메뉴 / 멤버 메뉴 선택
class MyDialog(QDialog): 
    def __init__(self):
        super().__init__()
        self.SetUp()

    def SetUp(self):
        QDialog.__init__(self)
        btn1 = QPushButton("1.클럽 메뉴")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.멤버 메뉴")
        btn2.clicked.connect(self.on_button2)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.label = QLabel()
        self.setLayout(layout)
    
    
    def on_button1(self):
        dlg = ClubDialog()
        dlg.exec_()    

    def on_button2(self):
        dlg=MemberDialog()
        dlg.exec_()  

#클럽 메뉴 선택시 화면 - 클럽 관리 / 게시판 관리
class ClubDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self): 
        QDialog.__init__(self)
        btn1 = QPushButton("1.클럽 관리")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.게시판 관리")
        btn2.clicked.connect(self.on_button2)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg = ClubManagement()
        dlg.exec_()    

    def on_button2(self):
        dlg=ClubBoardManagement()
        dlg.exec_()  

#클럽 관리 선택시 화면 - 클럽 등록/ 클럽 목록/ 클럽 수정 / 클럽 삭제 / 클럽 검색 / 클럽 가입 / 클럽 멤버 정보
class ClubManagement(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("1.클럽 등록")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.클럽 목록")
        btn2.clicked.connect(self.on_button2)
        btn3 = QPushButton("3.클럽 수정")
        btn3.clicked.connect(self.on_button3)
        btn4 = QPushButton("4.클럽 삭제")
        btn4.clicked.connect(self.on_button4)
        btn5 = QPushButton("5.클럽 검색")
        btn5.clicked.connect(self.on_button5)
        btn6 = QPushButton("6.클럽 가입")
        btn6.clicked.connect(self.on_button6)
        btn7 = QPushButton("7.클럽 멤버 정보")
        btn7.clicked.connect(self.on_button7)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        layout.addWidget(btn7)
        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg = ClubRegisterDialog()
        dlg.exec_()    

    def on_button2(self):
        dlg=ClubListDialog()
        dlg.exec_()
    
    def on_button3(self):
        dlg=ClubUpdateDialog()
        dlg.exec_()
    def on_button4(self):
        dlg=ClubDeleteDialog()
        dlg.exec_()
    def on_button5(self):
        dlg=ClubSearchDialog()
        dlg.exec_()
    def on_button6(self):
        dlg=ClubJoinDialog()
        dlg.exec_()
    def on_button7(self):
        dlg=ClubInfoDialog()
        dlg.exec_()

#게시판 관리 선택시 화면 - 게시판 등록/ 게시판 목록/ 게시판 수정 / 게시판 삭제
class ClubBoardManagement(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        QDialog.__init__(self)
        btn1 = QPushButton("1.게시판 등록")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.게시판 목록")
        btn2.clicked.connect(self.on_button2)
        btn3 = QPushButton("3.게시판 수정")
        btn3.clicked.connect(self.on_button3)
        btn4 = QPushButton("4.게시판 삭제")
        btn4.clicked.connect(self.on_button4)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg=Boardregister()
        dlg.exec_()    

    def on_button2(self):
        dlg=BoardList()
        dlg.exec_()

    def on_button3(self):
        dlg=Boardupdate()
        dlg.exec_()

    def on_button4(self):
        dlg=Boarddelete()
        dlg.exec_()

#게시판 등록 선택시 화면
class Boardregister(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("1. 게시판 등록")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("클럽장 이메일: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.clubname = self.lineEdit1.text()
        self.admin = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.board_name = self.lineEdit4.text()
        self.board_number = None
        s=BoardController.register_controller(domain.BoardEntity(self.clubname,self.board_name,self.board_number,self.admin),self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#게시판 목록 선택시 화면
class BoardList(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.member = None
        self.password = None
        self.board_list=[]

    def setupUI(self):
        self.layout = QGridLayout()
        self.setWindowTitle("2. 게시판 목록")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("이메일: ")
        label3 = QLabel("비밀번호: ")

        self.label4 = QLabel(" ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label1, 1, 0)
        self.layout.addWidget(self.lineEdit1, 1, 1)
        self.layout.addWidget(label2, 2, 0)
        self.layout.addWidget(self.lineEdit2, 2, 1)
        self.layout.addWidget(label3, 3, 0)
        self.layout.addWidget(self.lineEdit3, 3, 1)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.member = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        txt = BoardController.get_all_post(self.ClubName,self.member,self.password)
        #self.close()
        self.label4 = QLabel(str(txt))
        self.layout.addWidget(self.label4, 4, 1)
        self.setLayout(self.layout)
        QMessageBox.about(self,"결과",str(txt))
        self.close()

#게시판 수정 선택시 화면
class Boardupdate(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("3. 게시판 수정")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("클럽장: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")
        label5 = QLabel("수정할 게시판 이름: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.clubname = self.lineEdit1.text()
        self.admin = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.board_name = self.lineEdit4.text()
        self.change_board_name = self.lineEdit5.text()
        s=BoardController.update_controller(self.clubname,self.admin,self.board_name,self.password,self.change_board_name)
        QMessageBox.about(self,"결과",s)
        self.close()

#게시판 삭제 선택시 화면
class Boarddelete(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("4. 게시판 삭제")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("클럽장 이메일: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.clubname = self.lineEdit1.text()
        self.admin = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.board_name = self.lineEdit4.text()
        s=BoardController.delete_controller(self.clubname,self.board_name,self.admin,self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#멤버 메뉴 선택시 화면 - 회원관리/ 게시글 관리
class MemberDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self): 
        QDialog.__init__(self)
        btn1 = QPushButton("1.회원 관리")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.게시글 관리")
        btn2.clicked.connect(self.on_button2)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg = MemberManagement()
        dlg.exec_()    

    def on_button2(self):
        dlg=PostManagement()
        dlg.exec_()
    
#회원 관리 선택시 화면 - 멤버 등록/ 멤버 목록/ 멤버 수정/ 멤버 삭제/ 멤버 상세 정보/ 클럽 가입/ 클럽 탈퇴
class MemberManagement(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()   
    def setupUI(self): 
        QDialog.__init__(self)
        btn1 = QPushButton("1.멤버 등록")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.멤버 목록")
        btn2.clicked.connect(self.on_button2)
        btn3 = QPushButton("3.멤버 수정")
        btn3.clicked.connect(self.on_button3)
        btn4 = QPushButton("4.멤버 삭제")
        btn4.clicked.connect(self.on_button4)
        btn5 = QPushButton("5.멤버 상세 정보")
        btn5.clicked.connect(self.on_button5)
        btn6 = QPushButton("6.클럽 가입")
        btn6.clicked.connect(self.on_button6)
        btn7 = QPushButton("7.클럽 탈퇴")
        btn7.clicked.connect(self.on_button7)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        layout.addWidget(btn7)
        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg = MemberRegisterDialog()
        dlg.exec_()    
    def on_button2(self):
        dlg=MemberListDialog()
        dlg.exec_()  
    def on_button3(self):
        dlg=MemberUpdateDialog()
        dlg.exec_()
    def on_button4(self):
        dlg=MemberDeleteDialog()
        dlg.exec_()
    def on_button5(self):
        dlg=MemberInfoDialog()
        dlg.exec_()
    def on_button6(self):
        dlg=MemberJoinClubDialog()
        dlg.exec_()
    def on_button7(self):
        dlg=MemberOutDialog()
        dlg.exec_()

#게시글 관리 선택시 화면 - 게시글 등록/ 게시글 목록/ 게시글 수정/ 게시글 삭제
class PostManagement(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        QDialog.__init__(self)
        btn1 = QPushButton("1.게시글 등록")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.게시글 목록")
        btn2.clicked.connect(self.on_button2)
        btn3 = QPushButton("3.게시글 수정")
        btn3.clicked.connect(self.on_button3)
        btn4 = QPushButton("4.게시글 삭제")
        btn4.clicked.connect(self.on_button4)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        self.label = QLabel()
        self.setLayout(layout)

    def on_button1(self):
        dlg=PostRegister()
        dlg.exec_()    

    def on_button2(self):
        dlg=PostList()
        dlg.exec_()

    def on_button3(self):
        dlg=PostUpdate()
        dlg.exec_()

    def on_button4(self):
        dlg=PostDelete()
        dlg.exec_()

#게시글 등록 선택시 화면
class PostRegister(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.ClubName = None
        self.writer = None
        self.BoardName=None
        self.password=None
        self.PostName = None
        self.contents = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("1. 게시글 등록")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("작성자 이메일: ")
        label3 = QLabel("작성자 비밀번호: ")
        label4 = QLabel("게시판 이름: ")
        label5 = QLabel("게시글 이름: ")
        label6 = QLabel("내용: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.lineEdit6, 5, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.writer = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.BoardName = self.lineEdit4.text()
        self.PostName = self.lineEdit5.text()
        self.contents = self.lineEdit6.text()
        s=PostController.register_controller(domain.PostEntity(self.ClubName,self.BoardName,self.PostName,self.writer,self.contents),self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#게시글 목록 선택시 화면
class PostList(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.writer = None
        self.BoardName = None
        self.password = None
        self.post_list=[]

    def setupUI(self):
        self.layout = QGridLayout()
        self.setWindowTitle("2. 게시글 목록")
        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("이메일: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")

        self.label5 = QLabel(" ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label1, 1, 0)
        self.layout.addWidget(self.lineEdit1, 1, 1)
        self.layout.addWidget(label2, 2, 0)
        self.layout.addWidget(self.lineEdit2, 2, 1)
        self.layout.addWidget(label3, 3, 0)
        self.layout.addWidget(self.lineEdit3, 3, 1)
        self.layout.addWidget(label4, 4, 0)
        self.layout.addWidget(self.lineEdit4, 4, 1)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.member = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.BoardName = self.lineEdit4.text()
        self.txt = PostController.get_all_post(self.ClubName,self.BoardName,self.member,self.password)
        i=4
        for index in self.txt:
            self.label2 = QLabel(str(index))
            print(str(index))
            self.layout.addWidget(self.label2, i+1, 0)
            #model.appendRow(QStandardItem(str(index)))
            i+=1
        #self.label5 = QLabel(str(self.txt))
        #self.layout.addWidget(self.label5, 5, 1)
        self.setLayout(self.layout)

#게시글 수정 선택시 화면
class PostUpdate(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("3. 게시글 수정")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("작성자 이메일: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")
        label5 = QLabel("게시글 이름: ")
        label6 = QLabel("수정할 게시글 이름: ")
        label7 = QLabel("수정할 내용: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.lineEdit7 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.lineEdit6, 5, 1)
        layout.addWidget(label7, 6, 0)
        layout.addWidget(self.lineEdit7, 6, 1)
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.clubname = self.lineEdit1.text()
        self.writer = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.board_name = self.lineEdit4.text()
        self.post_name = self.lineEdit5.text()
        self.change_post_name = self.lineEdit6.text()
        self.change_content = self.lineEdit7.text()
        s=PostController.update_controller(self.clubname,self.writer,self.board_name,self.password,self.post_name,self.change_post_name,self.change_content)
        QMessageBox.about(self,"결과",s)
        self.close()

#게시글 삭제 선택시 화면
class PostDelete(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("4. 게시글 삭제")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("작성자 이메일: ")
        label3 = QLabel("비밀번호: ")
        label4 = QLabel("게시판 이름: ")
        label5 = QLabel("게시글 이름")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.clubname = self.lineEdit1.text()
        self.writer = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.board_name = self.lineEdit4.text()
        self.postname = self.lineEdit5.text()
        s=PostController.delete_controller(self.clubname,self.board_name,self.postname,self.writer,self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#클럽 등록 선택시 화면
class ClubRegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.ClubName = None
        self.intro = None
        self.leader=None
        self.FoundationDay=None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("1. 클럽 등록")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("클럽 정보: ")
        label3 = QLabel("클럽장 이메일: ")
        label5 = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5,4,1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.intro = self.lineEdit2.text()
        self.leader = self.lineEdit3.text()
        self.FoundationDay = None
        self.password = self.lineEdit5.text()
        s=Ccontroller.register_controller(domain.ClubEntity(self.ClubName,self.intro,self.leader,self.FoundationDay),self.password)
        QMessageBox.about(self,"결과",str(s))
        self.close()

#클럽 목록 선택시 화면
class ClubListDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.intro = None
        self.leader=None
        self.FoundationDay=None
        self.club_list=[]

    def setupUI(self):
        #self.setGeometry(1100, 200, 500, 100)
        self.setWindowTitle("2. 클럽 목록")
        layout = QGridLayout()
        listview = QListView(self)
        scrollArea = QScrollArea()
        listview.resize(500, 100)
        model = QStandardItemModel()
        self.club_list=Ccontroller.get_all_Club_entity_controller()
        for index in self.club_list:
            model.appendRow(QStandardItem(str(index)))
        #model.appendRow(QStandardItem(str(self.club_list[0])))
        listview.setModel(model)
    
        layout.addWidget(scrollArea)
        self.show()

    def pushButtonClicked(self):
        self.close()

#클럽 수정 선택시 화면
class ClubUpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.intro = None
        self.leader=None
        self.FoundationDay=None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("3. 수정")

        label1 = QLabel("클럽 이름: ")
        label2 = QLabel("클럽 정보: ")
        label3 = QLabel("클럽장 이메일: ")
        label4 = QLabel("클럽 생성일: ")
        label5 = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5,4, 0)
        layout.addWidget(self.lineEdit5,4,1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.intro = self.lineEdit2.text()
        self.leader = self.lineEdit3.text()
        self.FoundationDay = self.lineEdit4.text()
        self.password = self.lineEdit5.text()
        s=Ccontroller.update_controller(domain.ClubEntity(self.ClubName,self.intro,self.leader,self.FoundationDay),self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#클럽 삭제 선택시 화면
class ClubDeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("4. 클럽 삭제")

        label3 = QLabel("클럽 이름: ")
        label5 = QLabel("비밀번호: ")

        self.lineEdit3 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.pushButton1 = QPushButton("삭제")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()

        layout.addWidget(label3, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(label5, 2, 0)
        layout.addWidget(self.lineEdit5, 2, 1)
        layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit3.text()
        self.password = self.lineEdit5.text()
        s=Ccontroller.delete_controller(self.ClubName,self.password)
        QMessageBox.about(self,"결과",s)
        self.close()
        
#클럽 검색 선택시 화면
class ClubSearchDialog(QDialog):
    layout = QGridLayout()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName=None
        self.label2 = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.layout = QGridLayout()
        self.setWindowTitle("5. 클럽 상세 정보")

        label3 = QLabel("클럽 이름: ")
        #label1 = QLabel("검색결과: ")
        #self.label2 = QLabel(" ")
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label3, 1, 0)
        self.layout.addWidget(self.lineEdit3, 1, 1)
        #self.layout.addWidget(label1, 2, 0)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit3.text()
        txt = Ccontroller.get_club_entity_controller(self.ClubName)
        #print(txt)
        #self.close()
        #self.label2 = QLabel(str(txt))
        #self.layout.addWidget(self.label2, 2, 1)
        #self.setLayout(self.layout)
        QMessageBox.about(self,"결과",str(txt))
        self.close()

#클럽 가입 선택시 화면
class ClubJoinDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.joinDate = None
        self.email=None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("6. 클럽 가입")

        label1 = QLabel("클럽 이름: ")
        label3 = QLabel("이메일: ")
        label4 = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.joinDate = None
        self.email = self.lineEdit3.text()
        self.password = self.lineEdit4.text()
        s=CMcontroller.register_controller(domain.ClubMemberEntity(self.ClubName,self.joinDate,self.email),self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#클럽 멤버 정보 선택시 화면
class ClubInfoDialog(QDialog):
    layout = QGridLayout()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.club_list=[]
        self.label2 = None
    def setupUI(self):
        self.layout = QGridLayout()
        label3 = QLabel("클럽 이름: ")
        #label1 = QLabel("검색결과: ")
        self.label2 = QLabel(" ")
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label3, 1, 0)
        self.layout.addWidget(self.lineEdit3, 1, 1)
        #self.layout.addWidget(label1, 2, 0)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        QDialog.__init__(self)
        self.setWindowTitle("2. 클럽 목록")
        layout = QGridLayout()
        listview = QListView(self)
        scrollArea = QScrollArea()
        listview.resize(500, 100)
        model = QStandardItemModel()
        self.ClubName = self.lineEdit3.text()
        self.club_list = CMcontroller.get_entity_controller(self.ClubName)
        self.lineEdit3=None
        scrollArea = QScrollArea()
        #self.close()
        i=1
        for index in self.club_list:
            self.label2 = QLabel(str(index))
            print(str(index))
            self.layout.addWidget(self.label2, i+1, 0)
            #model.appendRow(QStandardItem(str(index)))
            i+=1
        listview.setModel(model)
    
        layout.addWidget(scrollArea)
        self.close()

#멤버 등록 선택시 화면
class MemberRegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.email = None
        self.MemberName = None
        self.PhoneNumber=None
        self.BirthDay=None
        self.address=None
        self.password=None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("1. 멤버 등록")

        label1 = QLabel("이메일: ")
        label2 = QLabel("이름: ")
        label3 = QLabel("전화번호: ")
        label4 = QLabel("생일: ")
        label5 = QLabel(" 주소")
        label6 = QLabel("비밀번호")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.pushButton1= QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.lineEdit6, 5, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit1.text()
        self.MemberName = self.lineEdit2.text()
        self.PhoneNumber = self.lineEdit3.text()
        self.BirthDay = self.lineEdit4.text()
        self.address = self.lineEdit5.text()
        self.password = self.lineEdit6.text()
        s=Mcontroller.register_controller(domain.MemberEntity(self.email,self.MemberName,self.PhoneNumber,self.BirthDay,self.address,self.password))
        print(s)
        QMessageBox.about(self,"결과",str(s))
        self.close()

#멤버 목록 선택시 화면
class MemberListDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email = None
        self.MemberName = None
        self.PhoneNumber=None
        self.BirhtDay=None
        self.address=None
        self.member_list=[]

    def setupUI(self):
        #self.setGeometry(1100, 200, 500, 100)
        self.setWindowTitle("2. 멤버 목록")
        layout = QGridLayout()
        listview = QListView(self)
        scrollArea = QScrollArea()
        listview.resize(500, 100)
        model = QStandardItemModel()
        self.member_list=Mcontroller.get_all_Member_entity_controller()
        for index in self.member_list:
            model.appendRow(QStandardItem(str(index)))
        #model.appendRow(QStandardItem(str(self.club_list[0])))
        listview.setModel(model)
    
        layout.addWidget(scrollArea)
        self.show()

    def pushButtonClicked(self):
        self.close()

#멤버 수정 선택시 화면
class MemberUpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email = None
        self.MemberName = None
        self.PhoneNumber=None
        self.BirthDay=None
        self.address=None
        self.password=None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("3. 수정")

        label1 = QLabel("이메일: ")
        label2 = QLabel("이름: ")
        label3 = QLabel("전화번호: ")
        label4 = QLabel("생일: ")
        label5 = QLabel("주소: ")
        label6 = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.lineEdit6, 5, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit1.text()
        self.MemberName = self.lineEdit2.text()
        self.PhoneNumber = self.lineEdit3.text()
        self.BirthDay = self.lineEdit4.text()
        self.address = self.lineEdit5.text()
        self.password = self.lineEdit6.text()
        s=Mcontroller.update_controller(domain.MemberEntity(self.email,self.MemberName,self.PhoneNumber,self.BirthDay,self.address,self.password))
        QMessageBox.about(self,"결과",s)
        self.close()

#멤버 삭제 선택시 화면
class MemberDeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email = None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("4. 삭제")

        label3 = QLabel("이메일: ")
        label2 = QLabel("비밀번호: ")

        self.lineEdit3 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1 = QPushButton("삭제")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()

        layout.addWidget(label3, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(self.pushButton1, 1, 2)
        layout.addWidget(label2, 2, 0)
        layout.addWidget(self.lineEdit2, 2, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit3.text()
        self.password = self.lineEdit2.text()
        s=Mcontroller.delete_controller(self.email,self.password)
        QMessageBox.about(self,"결과",s)
        self.close()
        
#멤버 상세 정보 선택시 화면
class MemberInfoDialog(QDialog):
    layout = QGridLayout()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email=None
        self.label2 = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.layout = QGridLayout()
        self.setWindowTitle("5. 멤버 상세 정보")

        label3 = QLabel("이메일: ")
        #label1 = QLabel("검색결과: ")
        #self.label2 = QLabel(" ")
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label3, 1, 0)
        self.layout.addWidget(self.lineEdit3, 1, 1)
        #self.layout.addWidget(label1, 2, 0)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit3.text()
        txt = Mcontroller.get_member_entity_controller(self.email)
        #self.close()
        #print(txt)
        #self.label2 = QLabel(str(txt))
        #self.layout.addWidget(self.label2, 2, 1)
        #self.setLayout(self.layout)
        QMessageBox.about(self,"결과",str(txt))
        self.close()

#클럽 가입 선택시 화면
class MemberJoinClubDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.ClubName = None
        self.joinDate = None
        self.email=None
        self.password = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("6. 클럽 가입")

        label1 = QLabel("클럽 이름: ")
        label3 = QLabel("이메일: ")
        label4 = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.pushButton1 = QPushButton("등록")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ClubName = self.lineEdit1.text()
        self.joinDate = None
        self.email = self.lineEdit3.text()
        self.password = self.lineEdit4.text()
        s=CMcontroller.register_controller(domain.ClubMemberEntity(self.ClubName,self.joinDate,self.email),self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

#클럽 탈퇴 선택시 화면
class MemberOutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.clubname = None
        self.password = None
        self.email = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("7. 탈퇴")

        label1 = QLabel("이메일: ")
        label3 = QLabel("클럽 이름: ")
        label2 = QLabel("비밀번호: ")

        self.lineEdit3 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit1 = QLineEdit()
        self.pushButton1 = QPushButton("삭제")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()

        layout.addWidget(label3, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(self.pushButton1, 1, 2)
        layout.addWidget(label1, 2, 0)
        layout.addWidget(self.lineEdit1, 2, 1)
        layout.addWidget(label2, 3, 0)
        layout.addWidget(self.lineEdit2, 3, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.clubname = self.lineEdit3.text()
        s=CMcontroller.delete_controller(self.clubname,self.email,self.password)
        QMessageBox.about(self,"결과",s)
        self.close()

app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()