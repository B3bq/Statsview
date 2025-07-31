from PySide6.QtGui import QPixmap, QCloseEvent, QIcon, QPalette, QColor
from PySide6.QtWidgets import *
from PySide6.QtCore import QRegularExpression
import re, datetime, json, os, random
import add_new, add_ex, summary_window
from insert import * # functions to insert user datas to database and check log in
from mail import * # import mail script



class Program(QWidget):
    def __init__(self):
        super().__init__()

        # setup buttons
        self.addEX_btn = QPushButton("Add Exists Teams", self)
        self.addEX_btn.setFixedSize(200, 50)
        self.addEX_btn.move(400, 50)
        self.addNew_btn = QPushButton("Add New Teams", self)
        self.addNew_btn.setFixedSize(200, 50)
        self.addNew_btn.move(400, 100)
        self.viewStats_btn_s = QPushButton("Season summary", self)
        self.viewStats_btn_s.setFixedSize(200, 50)
        self.viewStats_btn_s.move(400, 150)
        self.viewStats_btn_y = QPushButton("Year summary", self)
        self.viewStats_btn_y.setFixedSize(200, 50)
        self.viewStats_btn_y.move(400, 150)
        self.log_out_btn = QPushButton("Log out", self)
        self.log_out_btn.setFixedSize(200, 50)
        self.log_out_btn.move(400, 200)
        self.close_btn = QPushButton("Close", self)
        self.close_btn.setFixedSize(200, 50)
        self.close_btn.move(400, 250)

        # log in buttons
        self.btn_login = QPushButton("Log in", self)
        self.btn_login.setFixedSize(200, 50)
        self.btn_login.move(400, 200)
        self.btn_signin = QPushButton("Sign up", self)
        self.btn_signin.setFixedSize(200, 50)
        self.btn_signin.move(400, 250)

        # login input
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Login")
        self.name.setFixedSize(200, 50)
        # mail input
        self.mail = QLineEdit(self)
        self.mail.setPlaceholderText("E-mail")
        self.mail.setFixedSize(200, 50)
        self.mail.move(295, 100)
        # password input
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setFixedSize(200, 50)
        self.password.move(400, 100)
        # checkbox remember me
        self.remember_me = QCheckBox("Remember me", self)
        self.remember_me.move(400, 170)

        # back button
        self.back_btn = QPushButton("Back", self)
        self.back_btn.setFixedSize(100, 50)
        self.back_btn.move(295, 200)
        # password for create window
        self.password_create = QLineEdit(self)
        self.password_create.setEchoMode(QLineEdit.Password)
        self.password_create.setPlaceholderText("Password")
        self.password_create.setFixedSize(200, 50)
        self.password_create.move(505, 50)
        # reapet a password
        self.re_password = QLineEdit(self)
        self.re_password.setEchoMode(QLineEdit.Password)
        self.re_password.setPlaceholderText("Reapet password")
        self.re_password.setFixedSize(200, 50)
        self.re_password.move(505, 100)
        # verification code
        self.ver_code = QLineEdit(self)
        self.ver_code.setPlaceholderText("Enter verification code")
        self.ver_code.setFixedSize(200, 50)
        self.ver_code.move(400, 150)
        # label for verification
        self.label_ver = QLabel("Incorrect code", self)
        self.label_ver.move(458, 205)
        # verification button
        self.btn_verification = QPushButton("Verify", self)
        self.btn_verification.setCheckable(True)
        self.btn_verification.move(460, 220)
        #checkbox to show pass
        self.show_pass = QCheckBox("Show password", self)
        self.show_pass.move(400, 150)
        # create new account btn
        self.create_btn = QPushButton("Create account", self)
        self.create_btn.setFixedSize(100, 50)
        self.create_btn.move(600, 200)

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
        self.label1 = QLabel("User exist", self)
        self.label1.move(440, 215)
        self.label2 = QLabel("Passwords are incorrect", self)
        self.label2.move(440, 215)
        self.labelMail = QLabel("Incorrect e-mail address", self)
        self.labelMail.move(440, 215)


        # checking if user is log in
        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        # here must be if user is log in 
        if user_data["user_id"] != 0:
            self.setup() # true then show main screen
            User.user_id = user_data["user_id"] # set class user to user whose is remember
        else:
            self.login_screen() # false then show login screen

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))
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
        self.label1.hide()
        self.label2.hide()
        self.mail.hide()
        self.labelMail.hide()
        self.password_create.hide()
        self.addEX_btn.hide()
        self.addNew_btn.hide()
        self.viewStats_btn_s.hide()
        self.viewStats_btn_y.hide()
        self.log_out_btn.hide()
        self.close_btn.hide()
        self.ver_code.hide()
        self.label_ver.hide()
        self.btn_verification.hide()

        # reset user id
        User.user_id = ''

        # reset locl file which save user id
        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)

        user_data["user_id"] = 0

        with open(file_path, 'wt') as file:
            json.dump(user_data, file)

        #login
        self.name.clear()
        self.name.show()
        self.name.move(400, 50)

        #password
        self.password.clear()
        self.password.show()
        self.password.setPalette(QPalette()) 

        self.show_pass.move(400, 150)
        self.show_pass.show()
        self.show_pass.stateChanged.connect(self.toggle_password_visibility) # password visibility

        self.remember_me.show() # remember me button
        self.remember_me.clicked.connect(self.rem_me)

        #log in btn
        self.btn_login.show()
        self.btn_login.clicked.connect(self.check_user)

        #sign in btn
        self.btn_signin.show()
        self.btn_signin.clicked.connect(self.create_new)


    def create_new(self):
        # hiding login
        self.btn_login.hide()
        self.btn_signin.hide()
        self.ck_label.hide()
        self.ck_label2.hide()
        self.password.hide()
        self.remember_me.hide()
        self.ver_code.hide()
        self.label_ver.hide()
        self.ver_code.hide()

        # show needed elements
        self.re_password.show()
        self.mail.show()
        self.password_create.show()

        self.name.move(295, 50)
        self.show_pass.move(505, 160)

        # clearing inputs
        self.name.clear()
        self.mail.clear()
        self.password_create.clear()

        # checking a value of strong password
        self.password_create.textChanged.connect(self.pass_strong)

        self.re_password.clear()

        # checking mail is correctly wrote
        #self.mail.textChanged.connect(self.validate_mail)

        self.create_btn.show()
        self.create_btn.clicked.connect(self.pass_check)

        # back btn show
        self.back_btn.show()
        self.back_btn.clicked.connect(self.login_screen)

    def setup(self):

        #hiding login screen
        self.name.hide()
        self.password.hide()
        self.show_pass.hide()
        self.btn_login.hide()
        self.btn_signin.hide()
        self.mail.hide()
        self.password_create.hide()
        self.remember_me.hide()
        self.re_password.hide()
        self.create_btn.hide()
        self.back_btn.hide()
        self.back.hide()
        self.ck_label2.hide()
        self.ck_label.hide()
        self.label.hide()
        self.label1.hide()
        self.label2.hide()
        self.labelMail.hide()
        self.ver_code.hide()
        self.label_ver.hide()
        self.ver_code.hide()
        self.btn_verification.hide()
    

        # date for view statistics
        today = datetime.date.today()
        end_date = [datetime.date(datetime.date.today().year, 7, 31), datetime.date(datetime.date.today().year, 7, 15), datetime.date(datetime.date.today().year, 7, 16), datetime.date(datetime.date.today().year, 7, 17), datetime.date(datetime.date.today().year, 7, 18), datetime.date(datetime.date.today().year, 1, 1), datetime.date(datetime.date.today().year, 1, 2), datetime.date(datetime.date.today().year, 1, 3), datetime.date(datetime.date.today().year, 1, 4)]
        

        #menu
        self.addEX_btn.show()
        self.addEX_btn.clicked.connect(self.open_add_exist) # open file to insert exist

        self.addNew_btn.show()
        self.addNew_btn.clicked.connect(self.open_add_new) # open file to insert datas

        # checking date
        if today in end_date[:5]:
            User.season = 'season'
            self.viewStats_btn_y.hide()
            self.viewStats_btn_s.show()
            self.viewStats_btn_s.clicked.connect(self.open_summary)
        elif today in end_date[5:]:
            User.season = 'year'
            self.viewStats_btn_s.hide()
            self.viewStats_btn_y.show()
            self.viewStats_btn_y.clicked.connect(self.open_summary)
        else:
            self.viewStats_btn_s.hide()
            self.viewStats_btn_y.hide()

        #log out
        self.log_out_btn.show()
        self.log_out_btn.clicked.connect(self.login_screen)

        #close button
        self.close_btn.show()
        self.close_btn.clicked.connect(QApplication.instance().quit)

    #show pass function
    def toggle_password_visibility(self, state):
        if state == 2: # chackbox is checked
            self.password.setEchoMode(QLineEdit.Normal)
            self.password_create.setEchoMode(QLineEdit.Normal)
            self.re_password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
            self.password_create.setEchoMode(QLineEdit.Password)
            self.re_password.setEchoMode(QLineEdit.Password)

    # validate emial
    def pass_strong(self, signal):
        # level of password
        lvl = 0

        # lenght of pass
        if len(signal) >= 8:
            lvl+=1
        if len(signal) >= 12:
            lvl+=1

        # are a small or big letters
        if re.search(r"[a-z]", signal) and re.search(r"[A-Z]", signal):
            lvl+=1

        # are numbers
        if re.search(r"\d", signal):
            lvl+=1

        if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", signal):
            lvl+=1

        self.input_color(value=lvl)

    # changing input color
    def input_color(self, value):
        palette = self.password_create.palette()
        match value:
            case 1:
                # red
                palette.setColor(QPalette.Base, QColor('#e60000')) # set a color of input's background 
            case 2:
                # orange
                palette.setColor(QPalette.Base, QColor('#ffa31a'))
            case 3:
                # yellow
                palette.setColor(QPalette.Base, QColor('#ffff00'))
            case 4:
                # light green
                palette.setColor(QPalette.Base, QColor('#bfff00'))
            case 5:
                # green
                palette.setColor(QPalette.Base, QColor('#00ff00'))
            case _:
                palette.setColor(QPalette.Base, QColor('#2D2D2D'))
    
        self.password_create.setPalette(palette) 

    # remeber me
    def rem_me(self):
        # reading data from json file
        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)

        # taking user id
        password = self.password.text()
        login = self.name.text()

        user_id = check_user(login, password)
        if type(user_id) == int: 
            user_data["user_id"] = user_id
        else:
            user_data["user_id"] = 0
        
        with open(file_path, "wt") as file:
            json.dump(user_data, file)

    def check_user(self):
        password = self.password.text()
        login = self.name.text()

        # encrypting password
        User.user_id = check_user(login, password)

        if type(User.user_id) == int:
                # hiding screen
                self.name.hide()
                self.password.hide()
                self.show_pass.hide()
                self.btn_login.hide()
                self.btn_signin.hide()

                # open menu
                self.setup()
        elif User.user_id == "Incorrect password":
            self.ck_label.hide()
            self.ck_label2.show()
        elif User.user_id == "User don't exist":
            self.ck_label.show()
            self.ck_label2.hide()

    def pass_check(self):
        pass1 = self.password_create.text()
        pass2 = self.re_password.text()
        mail = self.mail.text().lower()
        login = self.name.text()
        self.label1.hide()
        self.label2.hide()
        self.labelMail.hide()
        

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if re.match(pattern, mail):
            if(pass1 == pass2):
                name = check_name(login) # checikng if login is free
                if name == True:
                    # sending verification code
                    self.code = random.randrange(1000, 9999) # generate a code
                    # sending email to user
                    sent = mail_sent(mail, self.code)

                    if sent == True:
                        # hide all
                        self.create_btn.hide()
                        self.back_btn.hide()
                        self.name.hide()
                        self.mail.hide()
                        self.password_create.hide()
                        self.re_password.hide()
                        self.show_pass.hide()
                        self.label1.hide()
                        self.ver_code.show()
                        self.btn_verification.show()
                        self.btn_verification.clicked.connect(self.verification_mail)
                else:
                    self.label1.show()   
            else:
                self.label2.show()
        else:
            self.labelMail.show()

    def verification_mail(self):
        # taking datas
        login = self.name.text()
        mail = self.mail.text()
        pass1 = self.password_create.text()
        user_ver_code = int(self.ver_code.text())

        # if code equal user code statment
        if self.code == user_ver_code:
            isuser = insert_user(login, mail, pass1)
            if(isuser == True):
                # hide useless things
                self.ver_code.hide()
                self.btn_verification.hide()
                self.label_ver.hide()

                # show info
                self.label.setText(f"Added user {login}")
                self.label.show()

                self.back.show()
                self.back.clicked.connect(self.login_screen)
        else:
            self.label_ver.show()

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