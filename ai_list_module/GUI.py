from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import controller
import view
import domain
controller = controller.AIController()

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.SetUp()

    def SetUp(self):
        QDialog.__init__(self)
        btn1 = QPushButton("1.등록")
        btn1.clicked.connect(self.on_button1)
        btn2 = QPushButton("2.목록")
        btn2.clicked.connect(self.on_button2)
        btn3 = QPushButton("3.수정")
        btn3.clicked.connect(self.on_button3)
        btn4 = QPushButton("4.삭제")
        btn4.clicked.connect(self.on_button4)
        btn5 = QPushButton("5.검색")
        btn5.clicked.connect(self.on_button5)
        btn6 = QPushButton("6.종료")
        btn6.clicked.connect(self.on_button6)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        layout.addWidget(btn6)
        self.label = QLabel()
        self.setLayout(layout)
    
    
    def on_button1(self):
        dlg = OneDialog()
        dlg.exec_()    

    def on_button2(self):
        dlg=TwoDialog()
        dlg.exec_()  
    def on_button3(self):
        dlg=ThreeDialog()
        dlg.exec_()
    def on_button4(self):
        dlg=FourDialog()
        dlg.exec_()
    def on_button5(self):
        dlg=FiveDialog()
        dlg.exec_()
    def on_button6(self):
        controller.close()
        self.close()
      
class OneDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.name = None
        self.age = None
        self.email=None
        self.major=None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("1. 등록")

        label1 = QLabel("이름: ")
        label2 = QLabel("나이: ")
        label3 = QLabel("이메일: ")
        label4 = QLabel("학과: ")

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
        self.name = self.lineEdit1.text()
        self.age = self.lineEdit2.text()
        self.email = self.lineEdit3.text()
        self.major = self.lineEdit4.text()
        controller.register_controller(domain.AIEntity(self.name,self.age,self.email,self.major))
        self.close()

class TwoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.name = None
        self.age = None
        self.email=None
        self.major=None
        self.student_list=[]

    def setupUI(self):
        #self.setGeometry(1100, 200, 500, 100)
        self.setWindowTitle("2. 목록")
        layout = QGridLayout()
        listview = QListView(self)
        scrollArea = QScrollArea()
        listview.resize(500, 100)
        model = QStandardItemModel()
        self.student_list=controller.get_all_entity_controller()
        for index in enumerate(self.student_list):
            model.appendRow(QStandardItem(str(self.student_list[index])))
        listview.setModel(model)
    
        layout.addWidget(scrollArea)
        self.show()

    def pushButtonClicked(self):
        self.close()

class ThreeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.name = None
        self.age = None
        self.email = None
        self.major = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("3. 수정")

        label1 = QLabel("이름: ")
        label2 = QLabel("나이: ")
        label3 = QLabel("이메일: ")
        label4 = QLabel("학과: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
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

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.name = self.lineEdit1.text()
        self.age = self.lineEdit2.text()
        self.email = self.lineEdit3.text()
        self.major = self.lineEdit4.text()
        controller.update_controller(domain.AIEntity(self.name, self.age, self.email, self.major))
        self.close()

class FourDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("4. 삭제")

        label3 = QLabel("이메일: ")

        self.lineEdit3 = QLineEdit()
        self.pushButton1 = QPushButton("삭제")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()

        layout.addWidget(label3, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit3.text()
        controller.delete_controller(self.email)
        self.close()
        
class FiveDialog(QDialog):
    layout = QGridLayout()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.email=None
        self.label2 = None

    def setupUI(self):
        #self.setGeometry(1100, 200, 300, 100)
        
        self.setWindowTitle("5. 검색")

        label3 = QLabel("이메일: ")
        label1 = QLabel("검색결과: ")
        self.label2 = QLabel(" ")
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("검색")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.layout.addWidget(label3, 1, 0)
        self.layout.addWidget(self.lineEdit3, 1, 1)
        self.layout.addWidget(label1, 2, 0)
        self.layout.addWidget(self.pushButton1, 1, 2)

        self.setLayout(self.layout)

    def pushButtonClicked(self):
        self.email = self.lineEdit3.text()
        txt = controller.get_entity_controller(self.email)
        print(txt)
        #self.close()
        self.label2 = QLabel(str(txt))
        self.layout.addWidget(self.label2, 2, 1)
        self.setLayout(self.layout)

app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()