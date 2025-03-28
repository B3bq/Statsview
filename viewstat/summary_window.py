from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
from PySide6.QtWidgets import *
from summary import *

class Summary(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        self.setup()

    def back_menu(self):
        self.menu.show()
        self.close()

    def setup(self):

        league_names = top_leagues()
        league_names = [name[0] for name in league_names]
        y = 100
        for i in range(0, len(league_names)):
            self.label_league = QLabel(f"{i+1}. {league_names[i]}", self)
            self.label_league.move(200 , y)
            y+=25

        teams_table = top_teams()
        teams_table = [name[0] for name in teams_table]
        y = 100
        for i in range(0, len(teams_table)):
            self.label_teams = QLabel(f"{i+1}. {teams_table[i]}", self)
            self.label_teams.move(800, y)
            y+=25
            

        # back to menu button
        back_btn = QPushButton("Back", self)
        back_btn.move(450, 300)
        back_btn.clicked.connect(self.back_menu)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")