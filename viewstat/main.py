from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):

        #league choose
        self.league_choose = QComboBox()
        self.league_choose.addItems(["opcja1, opcja2"])#make the choose list
        
        #input teams boxes
        self.team_one_input = QLineEdit("Team1", self)
        self.team_one_input.setFixedSize(150, 50)
        self.team_one_input.move(300, 150)

        self.team_two_input = QLineEdit("Team2", self)
        self.team_two_input.setFixedSize(150, 50)
        self.team_two_input.move(500, 150)

        #add to base button
        submit_btn = QPushButton("Submit", self)
        submit_btn.move(700, 300)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

        self.show()


if __name__ == "__main__":
    app = QApplication([])

program = Program()

app.exec()