from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
from PySide6.QtWidgets import *
from show_ex import show_leagues, show_teams
from insert import add_datas_to_base


class Add_Exist(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        # add more button
        self.add_more_btn = QPushButton("Add more", self)
        self.add_more_btn.move(670, 300)
        self.add_more_btn.hide()

        self.setup()

    def back(self): 
        self.menu.show()
        self.close()

    def take_league_name(self):
        league_name = [self.league_box.currentText()]

        team_names = show_teams(league_name)

        self.team_one_box.clear()
        self.team_two_box.clear()

        self.team_one_box.addItems(team_names)
        self.team_two_box.addItems(team_names)

    def submit(self):
        # taking a varibles
        league_name = self.league_box.currentText()
        first_team = self.team_one_box.currentText()
        second_team = self.team_two_box.currentText()

        add_datas_to_base(league_name, first_team, second_team) # insert datas to database

        # hide lists
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

        # show a old form
        self.LeagueLabel.show()
        self.league_box.show()
        self.TeamOneLabel.show()
        self.team_one_box.show()
        self.TeamTwoLabel.show()
        self.team_two_box.show()
        self.submit_btn.show()

    def setup(self):

        # choose league list
        self.LeagueLabel = QLabel("Choose a league:", self)
        self.LeagueLabel.move(255, 130)

        league_names = show_leagues()

        self.league_box = QComboBox(self)
        self.league_box.setPlaceholderText("Leagues")
        self.league_box.addItems(league_names) # adding opitons to list
        self.league_box.setFixedSize(150, 50)
        self.league_box.move(250, 150)
        self.league_box.currentTextChanged.connect(self.take_league_name)
        
        # choose team_one list
        self.TeamOneLabel = QLabel("Choose First Team:", self)
        self.TeamOneLabel.move(430, 130)

        self.team_one_box = QComboBox(self)
        self.team_one_box.setPlaceholderText("First team")
        self.team_one_box.setFixedSize(150, 50)
        self.team_one_box.move(425, 150)

        # choose team_two list
        self.TeamTwoLabel = QLabel("Choose Seond Team:", self)
        self.TeamTwoLabel.move(605, 130)

        self.team_two_box = QComboBox(self)
        self.team_two_box.setPlaceholderText("Second team")
        self.team_two_box.setFixedSize(150, 50)
        self.team_two_box.move(600, 150)

        # submit button
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.move(670, 300)
        self.submit_btn.clicked.connect(self.submit)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(250, 300)
        back_btn.clicked.connect(self.back)

        self.show()

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")