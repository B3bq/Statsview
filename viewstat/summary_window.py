from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
from PySide6.QtWidgets import *
from summary import *
import io
from PIL import Image

class Summary(QWidget):
    def __init__(self, menu):
        super().__init__()

        self.menu = menu

        self.setup()

    def back_menu(self):
        self.menu.show()
        self.close()

    def setup(self):
    
        # list of top 5 leagus
        top_league_text = QLabel("TOP 5 LEAGUES", self)
        top_league_text.move(200, 75)
        count_league_text = QLabel("Count", self)
        count_league_text.move(300, 85)
        league_names = top_leagues() # taking a list of tuples
        y = 100 # position y for each text
        # loop to show top 5
        for i, (name, count, img_data) in enumerate(league_names, start=1):
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte
                
                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image form BLOB
                # QLavel for image
                img_label = QLabel(self)
                img_label.setPixmap(pixmap.scaled(15, 15))
                img_label.move(285, y)
            label_league = QLabel(f"{i}. {name}", self)
            label_league.move(200 , y)
            count_league = QLabel(f"{count}", self)
            count_league.move(310, y)
            y+=25 # space between each numeral text
            i+=1

        # list of top 5 teams
        top_teams_text = QLabel("TOP 5 TEAMS", self)
        top_teams_text.move(700, 75)
        count_teams_text = QLabel("Count", self)
        count_teams_text.move(800, 85)
        teams_table = top_teams() # taking a list of tuples
        # the same like above
        y = 100
        # making this list
        for i, (name, count, img_data) in enumerate(teams_table, start=1):
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte

                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image from BLOB
                # Qlabel for image
                img_label = QLabel(self)
                img_label.setPixmap(pixmap.scaled(15, 15)) # think about a bigger size or table
                img_label.move(785, y)
            label_teams = QLabel(f"{i}. {name}", self)
            label_teams.move(700, y)
            count_team = QLabel(f"{count}", self)
            count_team.move(810, y)
            y+=25
            i+=1
            
        # showing the most watched home team
        top_home_text = QLabel("HOME FAVOURITE", self)
        top_home_text.move(440, 25)
        top_home = home_team()

        for name, count, img_data in top_home:
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte

                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image from BLOB
                # QLabel for image
                img_label = QLabel(self)
                img_label.setPixmap(pixmap.scaled(50, 50))
                img_label. move(465, 60)
            self.label_top_home = QLabel(f"{name} ({count})",self)
            self.label_top_home.move(465, 125)

        # shoing the most watched away team
        top_away_text = QLabel("YOUR TRAVELED WITH THEM MOST OFTEN", self)
        top_away_text.move(375, 150)
        top_away = away_team()

        for name, count, img_data in top_away:
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte

                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image from BLOB
                # QLabel for image
                img_label = QLabel(self)
                img_label.setPixmap(pixmap.scaled(50,50))
                img_label.move(465, 185)
            self.label_top_away = QLabel(f"{name} ({count})",self)
            self.label_top_away.move(465, 250)

        # back to menu button
        back_btn = QPushButton("Back", self)
        back_btn.move(450, 300)
        back_btn.clicked.connect(self.back_menu)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")