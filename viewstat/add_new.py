from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *
from insert_new import add_datas_to_base # import function


class Add_New(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        # add next button
        self.add_next = QPushButton("Add more", self)
        self.add_next.move(670, 300)
        self.add_next.hide()
        self.add_next.clicked.connect(self.setup)

        self.setup()

    def back(self):
        self.menu.show()
        self.close()

    def submit(self):
        # taking a varibles
        league_name = self.league_input.text()
        teamOne_name = self.team_one_input.text()
        teamTwo_name = self.team_two_input.text()

        add_datas_to_base(league_name, teamOne_name, teamTwo_name)

        # hidding inputs
        self.league_input.hide()
        self.team_one_input.hide()
        self.team_two_input.hide()
        self.submit_btn.hide()

        # show text and add more button
        self.label = QLabel(f"Added {teamOne_name} and {teamTwo_name} to the competition {league_name}", self)
        self.label.move(375, 150)
        self.label.show()
        self.add_next.show()

    def setup(self):

        #league choose
        self.league_input = QLineEdit(self)
        self.league_input.setPlaceholderText("League") #placeholder text for input
        self.league_input.setFixedSize(150, 50)
        self.league_input.move(250, 150)
        
        #input teams boxes
        self.team_one_input = QLineEdit(self)
        self.team_one_input.setPlaceholderText("Team One")
        self.team_one_input.setFixedSize(150, 50)
        self.team_one_input.move(425, 150)

        self.team_two_input = QLineEdit(self)
        self.team_two_input.setPlaceholderText("Team Two")
        self.team_two_input.setFixedSize(150, 50)
        self.team_two_input.move(600, 150)

        # submit button
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.move(670, 300)
        self.submit_btn.clicked.connect(self.submit)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(250, 300)
        back_btn.clicked.connect(self.back)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

