from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *
from insert import add_datas_to_base # import function


class Add_New(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        # add next button
        self.add_next = QPushButton("Add more", self)
        self.add_next.move(745, 300)
        self.add_next.hide()

        self.setup()

    def back(self):
        self.menu.show()
        self.close()

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

    def setup(self):

        # choose a sport
        self.SportLabel = QLabel("Choose a sport:", self)
        self.SportLabel.move(155, 130)

        self.sport_box = QComboBox(self)
        self.sport_box.setPlaceholderText("Sport")
        self.sport_box.addItems(["Football", "Basketball", "Counter Strike", "League of legends"])
        self.sport_box.setFixedSize(150, 50)
        self.sport_box.move(150, 150)

        #league choose
        self.league_input = QLineEdit(self)
        self.league_input.setPlaceholderText("League") #placeholder text for input
        self.league_input.setFixedSize(150, 50)
        self.league_input.move(325, 150)
        
        #input teams boxes
        self.team_one_input = QLineEdit(self)
        self.team_one_input.setPlaceholderText("Team One")
        self.team_one_input.setFixedSize(150, 50)
        self.team_one_input.move(500, 150)

        self.team_two_input = QLineEdit(self)
        self.team_two_input.setPlaceholderText("Team Two")
        self.team_two_input.setFixedSize(150, 50)
        self.team_two_input.move(675, 150)

        # submit button
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.move(745, 300)
        self.submit_btn.clicked.connect(self.submit)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(150, 300)
        back_btn.clicked.connect(self.back)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")