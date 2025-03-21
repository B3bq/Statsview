from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *


class Add_New(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        self.setup()

    def back(self):
        self.menu.show()
        self.close()

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
        submit_btn = QPushButton("Submit", self)
        submit_btn.move(670, 300)

        # back button
        back_btn =QPushButton("Back", self)
        back_btn.move(250, 300)
        back_btn.clicked.connect(self.back)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

