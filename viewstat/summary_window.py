from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import *
from summary import *
import os, json
from translator import Translator

class Summary(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        if user_data["lang"] != "":
            self.translator = Translator(user_data["lang"])
        else:
            self.translator = Translator("en")


        # choose a sport
        self.SportLabel = QLabel(self)
        self.SportLabel.move(420, 130)

        self.sport_box = QComboBox(self)
        self.sport_box.setPlaceholderText("Sport")
        self.sport_box.addItems(["Football", "Basketball", "Counter Strike", "League of legends"])
        self.sport_box.setFixedSize(150, 50)
        self.sport_box.move(415, 150)

        # submit choice
        self.submit_btn = QPushButton(self)
        self.submit_btn.move(500, 300)
        self.submit_btn.clicked.connect(self.summary)

        # summary properies
        self.top_league_text = QLabel(self)
        self.top_league_text.move(175, 75)
        self.count_league_text = QLabel(self)
        self.count_league_text.move(325, 85)
        self.top_teams_text = QLabel(self)
        self.top_teams_text.move(700, 75)
        self.count_teams_text = QLabel(self)
        self.count_teams_text.move(850, 85)
        self.top_home_text = QLabel(self)
        self.top_home_text.move(440, 25)
        self.top_away_text = QLabel(self)
        self.top_away_text.move(375, 150)

        # back to menu button
        self.back_btn = QPushButton(self)
        self.back_btn.clicked.connect(self.main_window.open_main_window)


        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))
        self.retranslate_ui()

        # change language
        self.lang_btn = QComboBox(self)
        self.lang_btn.addItems(["English", "Polski"])
        self.lang_btn.setFixedSize(80 ,50)
        self.lang_btn.move(900, 10)
        self.lang_btn.currentTextChanged.connect(self.switch_language)

        self.setup()

    def retranslate_ui(self):
        self.SportLabel.setText(self.tr("sport_label"))
        self.submit_btn.setText(self.tr("submit"))
        self.back_btn.setText(self.tr("back_btn"))
        self.top_league_text.setText(self.tr("top_leagues"))
        self.count_league_text.setText(self.tr("count"))
        self.top_teams_text.setText(self.tr("top_teams"))
        self.count_teams_text.setText(self.tr("count"))
        self.top_home_text.setText(self.tr("top_home"))
        self.top_away_text.setText(self.tr("top_away"))

    def switch_language(self):
        new_lang = self.lang_btn.currentText()
        if new_lang == "English":
            self.translator.set_language("en")
            
            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "en"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        else:
            self.translator.set_language("pl")

            file_path = os.path.join(os.path.dirname(__file__), 'save.json')
            with open(file_path, 'r') as file:
                user_data = json.load(file)
            
            user_data["lang"] = "pl"

            with open(file_path, "wt") as file:
                json.dump(user_data, file)
        self.retranslate_ui()

    def summary(self):

        # hiding
        self.SportLabel.hide()
        self.sport_box.hide()
        self.submit_btn.hide()
        self.back_btn.hide()

        # changing back button
        self.back_btn.move(450, 300)
        self.back_btn.show()

        # taking sport
        sport = self.sport_box.currentText()

        # list of top 5 leagus
        self.top_league_text.show()
        self.count_league_text.show()
        league_names = top_leagues(sport) # taking a list of tuples
        y = 100 # position y for each text
        # loop to show top 5
        for i, (name, count, img_data) in enumerate(league_names, start=1):
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte
                
                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image form BLOB
                # QLavel for image
                self.img_label = QLabel(self)
                self.img_label.setPixmap(pixmap.scaled(15, 15))
                self.img_label.move(300, y)
                self.img_label.show()
            self.label_league = QLabel(f"{i}. {name}", self)
            self.label_league.move(175 , y)
            self.label_league.show()
            self.count_league = QLabel(f"{count}", self)
            self.count_league.move(335, y)
            self.count_league.show()
            y+=25 # space between each numeral text
            i+=1

        # list of top 5 teams
        self.top_teams_text.show()
        self.count_teams_text.show()
        teams_table = top_teams(sport) # taking a list of tuples
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
                self.img_label = QLabel(self)
                self.img_label.setPixmap(pixmap.scaled(15, 15)) # think about a bigger size or table
                self.img_label.move(825, y)
                self.img_label.show()
            self.label_teams = QLabel(f"{i}. {name}", self)
            self.label_teams.move(700, y)
            self.label_teams.show()
            self.count_team = QLabel(f"{count}", self)
            self.count_team.move(860, y)
            self.count_team.show()
            y+=25
            i+=1
            
        # showing the most watched home team
        self.top_home_text.show()
        top_home = home_team(sport)

        for name, count, img_data in top_home:
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte

                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image from BLOB
                # QLabel for image
                self.img_label = QLabel(self)
                self.img_label.setPixmap(pixmap.scaled(50, 50))
                self.img_label. move(465, 60)
                self.img_label.show()
            self.label_top_home = QLabel(f"{name} ({count})",self)
            self.label_top_home.move(465, 125)
            self.label_top_home.show()

        # shoing the most watched away team
        self.top_away_text.show()
        top_away = away_team(sport)

        for name, count, img_data in top_away:
            if img_data:
                if isinstance(img_data, memoryview):
                    img_data = img_data.tobytes() # convert to byte

                pixmap = QPixmap()
                pixmap.loadFromData(img_data) # load an image from BLOB
                # QLabel for image
                self.img_label = QLabel(self)
                self.img_label.setPixmap(pixmap.scaled(50,50))
                self.img_label.move(465, 185)
                self.img_label.show()
            self.label_top_away = QLabel(f"{name} ({count})",self)
            self.label_top_away.move(465, 250)
            self.label_top_away.show()

    def setup(self):
        # hiding things
        self.top_league_text.hide()
        self.count_league_text.hide()
        self.top_teams_text.hide()
        self.count_teams_text.hide()
        self.top_home_text.hide()
        self.top_away_text.hide()
    
        # sport choose
        self.SportLabel.show()
        self.sport_box.show()

        # submit
        self.submit_btn.show()

        # back
        self.back_btn.move(400, 300)
        self.back_btn.show()

    def reset_summary(self):
        for child in self.findChildren(QLabel):
            child.hide()

        self.setup()