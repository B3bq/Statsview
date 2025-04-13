from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *
import datetime
import add_new, add_ex, summary_window
from insert import insert_user, check_user # functions to insert user datas to database and check log in 

class Program(QWidget):
    def __init__(self):
        super().__init__()

        # back button
        self.back_btn = QPushButton("Back", self)
        self.back_btn.setFixedSize(100, 50)
        self.back_btn.move(400, 250)
        # reapet a password
        self.re_password = QLineEdit(self)
        self.re_password.setEchoMode(QLineEdit.Password)
        self.re_password.setPlaceholderText("Reapet password")
        self.re_password.setFixedSize(200, 50)
        self.re_password.move(400, 150)
        #checkbox to show pass
        self.show_pass = QCheckBox("Show password", self)
        self.show_pass.move(400, 150)
        # create new account btn
        self.create_btn = QPushButton("Create account", self)
        self.create_btn.setFixedSize(100, 50)
        self.create_btn.move(500, 250)

        # things after add user
        self.label = QLabel("", self)
        self.label.move(460, 200)
        self.back = QPushButton("Back to log in", self)
        self.back.setFixedSize(200, 50)
        self.back.move(400, 250)

        # things to check user
        self.ck_label = QLabel("User don't exist", self)
        self.ck_label.move(400, 175)
        self.ck_label2 = QLabel("Incorrect password", self)
        self.ck_label2.move(400, 175)


        self.login_screen()

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        self.show()

    def login_screen(self):

        # hiding
        self.label.hide()
        self.back.hide()
        self.ck_label.hide()
        self.ck_label2.hide()
        self.back_btn.hide()
        self.re_password.hide()
        self.create_btn.hide()

        #logni
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Login")
        self.name.setFixedSize(200, 50)
        self.name.move(400, 50)
        self.name.show()

        #password
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setFixedSize(200, 50)
        self.password.move(400, 100)
        self.password.show()
        
        self.show_pass.move(400, 150)
        self.show_pass.show()
        self.show_pass.stateChanged.connect(self.toggle_password_visibility) 

        #log in btn
        self.btn_login = QPushButton("Log in", self)
        self.btn_login.setFixedSize(200, 50)
        self.btn_login.move(400, 200)
        self.btn_login.show()
        self.btn_login.clicked.connect(self.check_user)

        #sign in btn
        self.btn_signin = QPushButton("Sign up", self)
        self.btn_signin.setFixedSize(200, 50)
        self.btn_signin.move(400, 250)
        self.btn_signin.show()
        self.btn_signin.clicked.connect(self.create_new)


    def create_new(self):
        # hiding login
        self.btn_login.hide()
        self.btn_signin.hide()

        self.re_password.show()

        self.show_pass.move(400, 200)

        # clearing inputs
        self.name.clear()
        self.password.clear()
        self.re_password.clear()

        self.create_btn.show()
        self.create_btn.clicked.connect(self.pass_check)

        # back btn show
        self.back_btn.show()
        self.back_btn.clicked.connect(self.login_screen)

    def setup(self):

        #hiding login screen
        self.name.hide()
        self.password.hide()
        self.btn_login.hide()
        self.btn_signin.hide()
        self.show_pass.hide()
        self.ck_label.hide()
        self.ck_label2.hide()

        # date for view statistics
        end_date = [datetime.date(2025, 3, 29), datetime.date(2025, 6, 1), datetime.date(2025, 6, 2), datetime.date(2025, 6, 3), datetime.date(2025, 6, 4), datetime.date(2026, 1, 1), datetime.date(2026, 1, 2), datetime.date(2026, 1, 3), datetime.date(2026, 1, 4)]
        today = datetime.date.today()

        #menu
        addEX_btn = QPushButton("Add Exists Teams", self)
        addEX_btn.setFixedSize(200, 50)
        addEX_btn.move(400, 50)
        addEX_btn.show()
        addEX_btn.clicked.connect(self.open_add_exist) # open file to insert exist

        addNew_btn = QPushButton("Add New Teams", self)
        addNew_btn.setFixedSize(200, 50)
        addNew_btn.move(400, 100)
        addNew_btn.show()
        addNew_btn.clicked.connect(self.open_add_new) # open file to insert datas

        viewStats_btn_s = QPushButton("Season summary", self)
        viewStats_btn_s.setFixedSize(200, 50)
        viewStats_btn_s.move(400, 150)
        viewStats_btn_y = QPushButton("Year summary", self)
        viewStats_btn_y.setFixedSize(200, 50)
        viewStats_btn_y.move(400, 150)
        # checking date
        if today in end_date[:5]:
             viewStats_btn_y.hide()
             viewStats_btn_s.show()
             viewStats_btn_s.clicked.connect(self.open_summary)
        elif today in end_date[5:]:
             viewStats_btn_s.hide()
             viewStats_btn_y.show()
             viewStats_btn_y.clicked.connect(self.open_summary)
        else:
             viewStats_btn_s.hide()
             viewStats_btn_y.hide()

        #log out


        #close button
        close_btn = QPushButton("Close", self)
        close_btn.setFixedSize(200, 50)
        close_btn.move(400, 250)
        close_btn.show()
        close_btn.clicked.connect(QApplication.instance().quit)

    #show pass function
    def toggle_password_visibility(self, state):
        if state == 2: # chackbox is checked
            self.password.setEchoMode(QLineEdit.Normal)
            self.re_password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
            self.re_password.setEchoMode(QLineEdit.Password)

    def check_user(self):
        password = self.password.text()
        login = self.name.text()

        # encrypting password
        isuser = check_user(login, password)

        if isuser == True:
                # hiding screen
                self.name.hide()
                self.password.hide()
                self.show_pass.hide()
                self.btn_login.hide()
                self.btn_signin.hide()

                # open menu
                self.setup()
        elif isuser == "Incorrect password":
            self.ck_label.hide()
            self.ck_label2.show()
        elif isuser == "User don't exist":
            self.ck_label.show()
            self.ck_label2.hide()

    def pass_check(self):
        pass1 = self.password.text()
        pass2 = self.re_password.text()
        login = self.name.text()

        if(pass1 == pass2):
            isuser = insert_user(login, pass1)
            if(isuser == True):
                # hide all
                self.create_btn.hide()
                self.name.hide()
                self.password.hide()
                self.re_password.hide()
                self.show_pass.hide()

                # show info
                self.label.setText(f"Added user {login}")
                self.label.show()

                self.back.show()
                self.back.clicked.connect(self.login_screen)
            else:
                label = QLabel("User exist", self)
                label.move(490, 225)
                label.show()
        else:
            label = QLabel("Passwords are incorrect", self)
            label.move(400, 225)
            label.show()

    # close app event
    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "Do you want to close app",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#create message box
        
        #check what an user clicked
        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def open_add_new(self):
            self.add_window = add_new.Add_New(self)
            self.add_window.show()
            self.hide()

    def open_add_exist(self):
            self.add_window = add_ex.Add_Exist(self)
            self.add_window.show()
            self.hide()

    def open_summary(self):
         self.add_window = summary_window.Summary(self)
         self.add_window.show()
         self.hide()


if __name__ == "__main__":
    app = QApplication([])

program = Program()

app.exec()