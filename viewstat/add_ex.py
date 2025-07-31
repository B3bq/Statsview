from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
from PySide6.QtWidgets import *
import os
from show_ex import show_leagues, show_teams
from insert import add_datas_to_base


class Add_Exist(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        # add more button
        self.add_more_btn = QPushButton("Add more", self)
        self.add_more_btn.move(745, 300)
        self.add_more_btn.hide()
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))

        self.setup()

    def back(self): 
        self.menu.show()
        self.close()

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

        league_names = show_leagues(sport_name)

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
        self.label.move(365,150)
        self.label.show()
        self.add_more_btn.show()
        self.add_more_btn.clicked.connect(self.reset)

    def reset(self):
        # hide text and button
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

    def setup(self):

        # choose a sport
        self.SportLabel = QLabel("Choose a sport:", self)
        self.SportLabel.move(155, 130)

        self.sport_box = QComboBox(self)
        self.sport_box.setPlaceholderText("Sport")
        self.sport_box.addItems(["Football", "Basketball", "Counter Strike", "League of legends"])
        self.sport_box.setFixedSize(150, 50)
        self.sport_box.move(150, 150)
        self.sport_box.currentTextChanged.connect(self.take_sport)

        # choose league list
        self.LeagueLabel = QLabel("Choose a league:", self)
        self.LeagueLabel.move(330, 130)


        self.league_box = QComboBox(self)
        self.league_box.setPlaceholderText("Leagues")
        self.league_box.setFixedSize(150, 50)
        self.league_box.move(325, 150)
        self.league_box.currentTextChanged.connect(self.take_league_name)
        
        # choose team_one list
        self.TeamOneLabel = QLabel("Choose First Team:", self)
        self.TeamOneLabel.move(505, 130)

        self.team_one_box = QComboBox(self)
        self.team_one_box.setPlaceholderText("First team")
        self.team_one_box.setFixedSize(150, 50)
        self.team_one_box.move(500, 150)

        # choose team_two list
        self.TeamTwoLabel = QLabel("Choose Seond Team:", self)
        self.TeamTwoLabel.move(680, 130)

        self.team_two_box = QComboBox(self)
        self.team_two_box.setPlaceholderText("Second team")
        self.team_two_box.setFixedSize(150, 50)
        self.team_two_box.move(675, 150)

        # submit button
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.move(745, 300)
        self.submit_btn.clicked.connect(self.submit)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(150, 300)
        back_btn.clicked.connect(self.back)

        self.show()

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")