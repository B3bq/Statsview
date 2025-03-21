from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
from PySide6.QtWidgets import *


class Add_Exist(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        self.setup()

    def back(self): 
        self.menu.show()
        self.close()

    def setup(self):

        # choose league list
        self.LeagueLabel = QLabel("Choose a league:", self)
        self.LeagueLabel.move(255, 130)

        self.league_box = QComboBox(self)
        self.league_box.addItems(["1", "2", "3"]) # adding opitons to list
        self.league_box.setFixedSize(150, 50)
        self.league_box.move(250, 150)
        
        # choose team_one list
        self.TeamOneLabel = QLabel("Choose First Team:", self)
        self.TeamOneLabel.move(430, 130)

        self.team_one_box = QComboBox(self)
        self.team_one_box.addItems([])
        self.team_one_box.setFixedSize(150, 50)
        self.team_one_box.move(425, 150)

        # choose team_two list
        self.TeamTwoLabel = QLabel("Choose Seond Team:", self)
        self.TeamTwoLabel.move(605, 130)

        self.team_two_box = QComboBox(self)
        self.team_two_box.addItems([])
        self.team_two_box.setFixedSize(150, 50)
        self.team_two_box.move(600, 150)

        # submit button
        submit_btn = QPushButton("Submit", self)
        submit_btn.move(670, 300)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(250, 300)
        back_btn.clicked.connect(self.back)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

    