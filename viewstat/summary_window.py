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
        y = 100
        i = 1
        for name, count in league_names:
            self.label_league = QLabel(f"{i}. {name} {count}", self)
            self.label_league.move(200 , y)
            y+=25
            i+=1

        teams_table = top_teams()
        y = 100
        i = 1
        for name, count in teams_table:
            self.label_teams = QLabel(f"{i}. {name} {count}", self)
            self.label_teams.move(800, y)
            y+=25
            i+=1
            
        top_home = home_team()

        for name, count in top_home:
            self.label_top_home = QLabel(f"{name} {count}",self)
            self.label_top_home.move(450, 150)

        top_away = away_team()

        for name, count in top_away:
            self.label_top_away = QLabel(f"{name} {count}",self)
            self.label_top_away.move(450, 250)

        # back to menu button
        back_btn = QPushButton("Back", self)
        back_btn.move(450, 300)
        back_btn.clicked.connect(self.back_menu)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")