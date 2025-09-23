from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
import os, json
from show_ex import show_leagues, show_teams
from insert import add_datas_to_base
from translator import Translator

class Add_Exist(QWidget):
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

        # add more button
        self.add_more_btn = QPushButton(self)
        self.add_more_btn.move(745, 300)
        self.add_more_btn.hide()
        
        # choose a sport
        self.SportLabel = QLabel(self)
        self.SportLabel.move(155, 130)

        self.sport_box = QComboBox(self)
        self.sport_box.setPlaceholderText("Sport")
        self.sport_box.addItems(["Football", "Basketball", "Volleyball", "Handball", "Counter Strike", "League of legends"])
        self.sport_box.setFixedSize(150, 50)
        self.sport_box.move(150, 150)
        self.sport_box.currentTextChanged.connect(self.take_sport)

        self.annonation = QLabel("No data", self)
        self.annonation.move(465, 230)
        self.annonation.hide()

        # choose league list
        self.LeagueLabel = QLabel(self)
        self.LeagueLabel.move(330, 130)

        self.league_box = QComboBox(self)
        self.league_box.setFixedSize(150, 50)
        self.league_box.move(325, 150)
        self.league_box.currentTextChanged.connect(self.take_league_name)

        # choose team_one list
        self.TeamOneLabel = QLabel(self)
        self.TeamOneLabel.move(505, 130)

        self.team_one_box = QComboBox(self)
        self.team_one_box.setFixedSize(150, 50)
        self.team_one_box.move(500, 150)

        # choose team_two list
        self.TeamTwoLabel = QLabel(self)
        self.TeamTwoLabel.move(680, 130)

        self.team_two_box = QComboBox(self)
        self.team_two_box.setFixedSize(150, 50)
        self.team_two_box.move(675, 150)

        # submit button
        self.submit_btn = QPushButton(self)
        self.submit_btn.move(745, 300)
        self.submit_btn.clicked.connect(self.submit)

        # text
        self.label = QLabel(self)
        self.label.move(365,150)

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
        
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))
        self.retranslate_ui()


    def retranslate_ui(self):
        self.add_more_btn.setText(self.tr("add_more"))
        self.SportLabel.setText(self.tr("sport_label"))
        self.LeagueLabel.setText(self.tr("league_label"))
        self.league_box.setPlaceholderText(self.tr("league"))
        self.TeamOneLabel.setText(self.tr("team_one_label"))
        self.team_one_box.setPlaceholderText(self.tr("team_one"))
        self.TeamTwoLabel.setText(self.tr("team_two_label"))
        self.team_two_box.setPlaceholderText(self.tr("team_two"))
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


    def take_league_name(self):
        league_name = [self.league_box.currentText()]
        sport_name = self.sport_box.currentText()

        team_names = show_teams(league_name, sport_name)

        self.team_one_box.clear()
        self.team_two_box.clear()

        self.team_one_box.addItems(team_names)
        self.team_two_box.addItems(team_names)

    def take_sport(self):
        sport_name = self.sport_box.currentText()
        self.league_box.clear()
        self.annonation.hide()

        league_names = show_leagues(sport_name)

        if league_names == []:
            self.annonation.show()

        self.league_box.addItems(league_names)

    def submit(self):
        # taking a varibles
        sport_name = self.sport_box.currentText()
        league_name = self.league_box.currentText()
        first_team = self.team_one_box.currentText()
        second_team = self.team_two_box.currentText()

        add_datas_to_base(sport_name, league_name=league_name, teamOne_name=first_team, teamTwo_name=second_team) # insert datas to database

        # hide lists
        self.SportLabel.hide()
        self.sport_box.hide()
        self.LeagueLabel.hide()
        self.TeamOneLabel.hide()
        self.TeamTwoLabel.hide()
        self.league_box.hide()
        self.team_one_box.hide()
        self.team_two_box.hide()
        self.submit_btn.hide()

        # show text and add more button
        self.label = QLabel(f"Added {first_team} and {second_team} to the competition {league_name}", self)
        self.label.show()
        self.add_more_btn.show()
        self.add_more_btn.clicked.connect(self.reset)

    def reset(self):
        # hide text and button
        if self.label.isVisible():
            self.label.hide()
            self.add_more_btn.hide()

        self.league_box.clear()

        # show a old form
        self.SportLabel.show()
        self.sport_box.show()
        self.LeagueLabel.show()
        self.league_box.show()
        self.TeamOneLabel.show()
        self.team_one_box.show()
        self.TeamTwoLabel.show()
        self.team_two_box.show()
        self.submit_btn.show()