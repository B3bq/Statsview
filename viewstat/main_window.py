from PySide6.QtGui import  QPalette, QColor, QIcon, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
import re, datetime, json, os, random
from insert import * # functions to insert user datas to database and check log in
from mail import * # import mail script
from connect import connect
from mysql.connector import Error
import requests
import webbrowser

APP_VERSION = '1.0.0'
UPDATE_URL = ''

file_path = os.path.join(os.path.dirname(__file__), 'save.json')
with open(file_path, 'r') as file:
    user_data = json.load(file)
class Main_window(QWidget):
    def __init__(self, main_window, translator):
        super().__init__()
        self.main_window = main_window
        self.translator = translator

        # setup buttons
        self.addEX_btn = QPushButton(self)
        self.addEX_btn.setFixedSize(200, 50)
        self.addEX_btn.move(400, 50)
        self.addNew_btn = QPushButton(self)
        self.addNew_btn.setFixedSize(200, 50)
        self.addNew_btn.move(400, 100)
        self.viewStats_btn_s = QPushButton(self)
        self.viewStats_btn_s.setFixedSize(200, 50)
        self.viewStats_btn_s.move(400, 150)
        self.viewStats_btn_y = QPushButton(self)
        self.viewStats_btn_y.setFixedSize(200, 50)
        self.viewStats_btn_y.move(400, 150)
        self.log_out_btn = QPushButton(self)
        self.log_out_btn.setFixedSize(200, 50)
        self.log_out_btn.move(400, 200)
        self.close_btn = QPushButton(self)
        self.close_btn.setFixedSize(200, 50)
        self.close_btn.move(400, 250)

        # log in buttons
        self.btn_login = QPushButton(self)
        self.btn_login.setFixedSize(200, 50)
        self.btn_login.move(400, 200)
        self.btn_signin = QPushButton(self)
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
        self.password.setFixedSize(200, 50)
        self.password.move(400, 100)
        # checkbox remember me
        self.remember_me = QCheckBox("Re_me", self)
        self.remember_me.setMinimumWidth(150)
        self.remember_me.move(400, 170)

        # back button
        self.back_btn = QPushButton(self)
        self.back_btn.setFixedSize(100, 50)
        self.back_btn.move(295, 200)
        # password for create window
        self.password_create = QLineEdit(self)
        self.password_create.setEchoMode(QLineEdit.Password)
        self.password_create.setFixedSize(200, 50)
        self.password_create.move(505, 50)
        # reapet a password
        self.re_password = QLineEdit(self)
        self.re_password.setEchoMode(QLineEdit.Password)
        self.re_password.setFixedSize(200, 50)
        self.re_password.move(505, 100)
        # verification code
        self.ver_code = QLineEdit(self)
        self.ver_code.setFixedSize(200, 50)
        self.ver_code.move(400, 150)
        # label for verification
        self.label_ver = QLabel(self)
        self.label_ver.move(458, 205)
        # verification button
        self.btn_verification = QPushButton(self)
        self.btn_verification.setCheckable(True)
        self.btn_verification.move(460, 220)
        #checkbox to show pass
        self.show_pass = QCheckBox("show", self)
        self.show_pass.setMinimumWidth(150)
        self.show_pass.move(400, 150)
        # create new account btn
        self.create_btn = QPushButton(self)
        self.create_btn.setFixedSize(100, 50)
        self.create_btn.move(600, 200)

        # things after add user
        self.label = QLabel("", self)
        self.label.move(460, 200)
        self.back = QPushButton(self)
        self.back.setFixedSize(200, 50)
        self.back.move(400, 250)

        # things to check user
        self.ck_label = QLabel(self)
        self.ck_label.setMinimumWidth(200)
        self.ck_label.move(455, 183)
        self.ck_label2 = QLabel(self)
        self.ck_label2.setMinimumWidth(200)
        self.ck_label2.move(455, 183)
        self.label1 = QLabel(self)
        self.label1.move(440, 215)
        self.label2 = QLabel(self)
        self.label2.setMinimumWidth(250)
        self.label2.move(440, 215)
        self.labelMail = QLabel(self)
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

        # change language
        img_src = os.path.join(os.path.dirname(__file__), 'languages.png')

        self.lang_btn = QComboBox(self)
        self.lang_btn.addItem(QIcon(img_src), "")
        self.lang_btn.addItems(["English", "Polski"])
        self.lang_btn.setCurrentIndex(0)
        self.lang_btn.activated.connect(self.on_lang_selected)
        self.lang_btn.setFixedSize(80 ,50)
        self.lang_btn.move(900, 10)

        model = self.lang_btn.model()
        for i in range(model.rowCount()):
            item = model.item(i)
            item.setTextAlignment(Qt.AlignCenter)

        self.lang_btn.currentTextChanged.connect(self.switch_language)


        self.retranslate_ui() # language

    def on_lang_selected(self, index):
        if index == 0:
            self.lang_btn.setCurrentIndex(0)

    def retranslate_ui(self):
        # action screen
        self.addEX_btn.setText(self.translator.tr("addEx"))
        self.addNew_btn.setText(self.translator.tr("addNew"))
        self.viewStats_btn_s.setText(self.translator.tr("viewStats_s"))
        self.viewStats_btn_y.setText(self.translator.tr("viewStats_y"))
        self.log_out_btn.setText(self.translator.tr("log_out"))
        self.close_btn.setText(self.translator.tr("close"))

        self.back_btn.setText(self.translator.tr("back_btn"))
        self.back.setText(self.translator.tr("back"))

        # log in screen
        self.btn_login.setText(self.translator.tr("btn_login"))
        self.btn_signin.setText(self.translator.tr("btn_signin"))

        # pass
        self.password.setPlaceholderText(self.translator.tr("password"))
        self.remember_me.setText(self.translator.tr("remember_me"))
        self.password_create.setPlaceholderText(self.translator.tr("password"))
        self.re_password.setPlaceholderText(self.translator.tr("re_pass"))
        self.show_pass.setText(self.translator.tr("show_pass"))

        # code
        self.ver_code.setPlaceholderText(self.translator.tr("ver_code"))
        self.label_ver.setText(self.translator.tr("label_ver"))
        self.btn_verification.setText(self.translator.tr("btn_ver"))
        self.create_btn.setText(self.translator.tr("create_btn"))

        self.ck_label.setText(self.translator.tr("ck_label"))
        self.ck_label2.setText(self.translator.tr("ck_label2"))
        self.label1.setText(self.translator.tr("label1"))
        self.label2.setText(self.translator.tr("label2"))
        self.labelMail.setText(self.translator.tr("labelMail"))
        self.lang_btn.setPlaceholderText(self.translator.tr("lang"))

    def switch_language(self):
        new_lang = self.lang_btn.currentText()
        if new_lang == "English":
            self.main_window.lang_change('en')
            
            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "en"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        else:
            self.main_window.lang_change("pl")

            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "pl"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        self.retranslate_ui()

    # checking database connection
    def check_connection(self):
        try:
            connection = connect()
            if connection.is_connected():
                connection.close()
        except:
            self.show_message(user_data['lang'])

    def show_message(self, lang):
        msg = QMessageBox(self)
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        msg.setWindowIcon(QIcon(icon_path))
        
        if lang=='en':
            msg.setWindowTitle("Connection Error")
            msg.setText("Cannot connect to database")
        else:
            msg.setWindowTitle("Błąd połączenia")
            msg.setText("Błąd połaczenia z bazą")
            
        msg.exec_()

    def check_for_updates(self):
        try:
            response = requests.get(UPDATE_URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                latest_version = data['version']
                download_url = data['url']
                changelog = data.get("changelog", "")

                if latest_version != APP_VERSION:
                    msg = QMessageBox()
                    base_path = os.path.dirname(os.path.abspath(__file__))
                    icon_path = os.path.join(base_path, "logo.svg")
                    msg.setWindowIcon(QIcon(icon_path))
                    if user_data['lang'] == 'en':
                        msg.setWindowTitle("Update available")
                        msg.setText(f"New version available: {latest_version}n\Current version: {APP_VERSION}")
                        msg.setInformativeText(f"Changes: \n{changelog}")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        ok_button = msg.button(QMessageBox.Ok)
                        cancel_button = msg.button(QMessageBox.Cancel)
                        ok_button.button(QMessageBox.Ok).setText("Download")
                        cancel_button.button(QMessageBox.Cancel).setText("Later")
                    else:
                        msg.setWindowTitle("Dostępna aktualizacja")
                        msg.setText(f"Dostępna nowa wersja: {latest_version}n\Obecna wersja: {APP_VERSION}")
                        msg.setInformativeText(f"Zmiany: \n{changelog}")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        ok_button = msg.button(QMessageBox.Ok)
                        cancel_button = msg.button(QMessageBox.Cancel)
                        ok_button.button(QMessageBox.Ok).setText("Pobierz")
                        cancel_button.button(QMessageBox.Cancel).setText("Póżniej")

                    result = msg.exec()

                    if result == QMessageBox.Ok:
                        webbrowser.open(download_url)
        except Exception as e:
            print("Nie udało się sprawdzić: ", e)

    def login_screen(self):
        self.check_connection()
        self.check_for_updates()

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
        self.check_connection()
        self.check_for_updates()

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
        end_date = [datetime.date(datetime.date.today().year, 9, 24), datetime.date(datetime.date.today().year, 7, 15), datetime.date(datetime.date.today().year, 7, 16), datetime.date(datetime.date.today().year, 7, 17), datetime.date(datetime.date.today().year, 7, 18), datetime.date(datetime.date.today().year, 1, 1), datetime.date(datetime.date.today().year, 1, 2), datetime.date(datetime.date.today().year, 1, 3), datetime.date(datetime.date.today().year, 1, 4)]
        

        #menu
        self.addEX_btn.show()
        self.addEX_btn.clicked.connect(self.main_window.open_add_exist) # open file to insert exist

        self.addNew_btn.show()
        self.addNew_btn.clicked.connect(self.main_window.open_add_new) # open file to insert datas

        # checking date
        if today in end_date[:5]:
            User.season = 'season'
            self.viewStats_btn_y.hide()
            self.viewStats_btn_s.show()
            self.viewStats_btn_s.clicked.connect(self.main_window.open_summary)
        elif today in end_date[5:]:
            User.season = 'year'
            self.viewStats_btn_s.hide()
            self.viewStats_btn_y.show()
            self.viewStats_btn_y.clicked.connect(self.main_window.open_summary)
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

                file_path = os.path.join(os.path.dirname(__file__), 'save.json')
                with open(file_path, 'r') as file:
                    user_data = json.load(file)

                # show info
                if user_data["lang"] == "en":
                    self.label.setText(f"Added user {login}")
                else:
                    self.label.setText(f"Dodano użytkownika {login}")
                self.label.show()

                self.back.show()
                self.back.clicked.connect(self.login_screen)
        else:
            self.label_ver.show()