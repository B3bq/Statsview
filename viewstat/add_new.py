from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
import os, json
from insert import add_datas_to_base # import function
from translator import Translator


class Add_New(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        if user_data["lang"] != "":
            self.translator = Translator(user_data["lang"])
        else:
            self.translator = Translator("en")


        # add next button
        self.add_next = QPushButton(self)
        self.add_next.move(745, 300)
        self.add_next.hide()
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))

        # choose a sport
        self.SportLabel = QLabel(self)
        self.SportLabel.move(155, 130)

        self.sport_box = QComboBox(self)
        self.sport_box.setPlaceholderText("Sport")
        self.sport_box.addItems(["Football", "Basketball", "Volleyball", "Handball", "Counter Strike", "League of legends"])
        self.sport_box.setFixedSize(150, 50)
        self.sport_box.move(150, 150)

        #league choose
        self.league_input = QLineEdit(self)
        self.league_input.setFixedSize(150, 50)
        self.league_input.move(325, 150)
        
        #input teams boxes
        self.team_one_input = QLineEdit(self)
        self.team_one_input.setFixedSize(150, 50)
        self.team_one_input.move(500, 150)

        self.team_two_input = QLineEdit(self)
        self.team_two_input.setFixedSize(150, 50)
        self.team_two_input.move(675, 150)

        # submit button
        self.submit_btn = QPushButton(self)
        self.submit_btn.move(745, 300)
        self.submit_btn.clicked.connect(self.submit)

        # text
        self.label = QLabel(self)

        # back button
        self.back_btn =QPushButton(self)
        self.back_btn.move(150, 300)
        self.back_btn.clicked.connect(self.main_window.open_main_window)

        # change language
        self.lang_btn = QComboBox(self)
        self.lang_btn.addItems(["English", "Polski"])
        self.lang_btn.setFixedSize(80 ,50)
        self.lang_btn.move(900, 10)
        self.lang_btn.currentTextChanged.connect(self.switch_language)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))
        self.retranslate_ui()

    def retranslate_ui(self):
        self.add_next.setText(self.tr("add_more"))
        self.SportLabel.setText("sport_label")
        self.league_input.setPlaceholderText(self.tr("league"))
        self.team_one_input.setPlaceholderText(self.tr("team_one"))
        self.team_two_input.setPlaceholderText(self.tr("team_two"))
        self.submit_btn.setText(self.tr("submit"))
        self.back_btn.setText(self.tr("back_btn"))

    def switch_language(self):
        new_lang = self.lang_btn.currentText()
        if new_lang == "English":
            self.translator.set_language("en")
            
            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "en"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        else:
            self.translator.set_language("pl")

            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "pl"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        self.retranslate_ui()

    def submit(self):
        # taking a varibles
        sport_name = self.sport_box.currentText()
        league_name = self.league_input.text()
        teamOne_name = self.team_one_input.text()
        teamTwo_name = self.team_two_input.text()

        add_datas_to_base(sport_name, league_name=league_name, teamOne_name=teamOne_name, teamTwo_name=teamTwo_name) # insert datas to database

        # hidding inputs
        self.SportLabel.hide()
        self.sport_box.hide()
        self.league_input.hide()
        self.team_one_input.hide()
        self.team_two_input.hide()
        self.submit_btn.hide()

        # show text and add more button
        self.label = QLabel(f"Added {teamOne_name} and {teamTwo_name} to the competition {league_name}", self)
        self.label.move(365, 150)
        self.label.show()
        self.add_next.show()
        self.add_next.clicked.connect(self.restart)

    def restart(self):
        # hide text and add button
        if self.label.isVisible():
            self.label.hide()
            self.add_next.hide()

        # show and clear inputs
        self.league_input.clear()
        self.team_one_input.clear()
        self.team_two_input.clear()
        
        self.SportLabel.show()
        self.sport_box.show()
        self.league_input.show()
        self.team_one_input.show()
        self.team_two_input.show()
        self.submit_btn.show()        