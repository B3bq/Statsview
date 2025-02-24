from PySide6.QtGui import QCloseEvent, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QLabel, QLineEdit

#class LoginWindow, all things for app
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.login_line_edit = QLabel

        self.setup()

    #making a layout
    def setup(self):
        width = 400

        #how to import a image
        pix_label = QLabel(self)
        pixmap = QPixmap("C:/Users/Sebastian/Documents/heb.png").scaled(150, 150)
        pix_label.setPixmap(pixmap)
        pix_label.move((width - 150)/2, 50)

        #create textboxes
        self.login_line_edit = QLineEdit("text", self)
        self.login_line_edit.setFixedHeight(50)
        self.login_line_edit.move(100, 250)

        pass_line_edit = QLineEdit("text", self)
        pass_line_edit.setFixedHeight(50)
        pass_line_edit.move(100, 320)

        #create the button to show a text from textboxes
        submit_btn = QPushButton("submit", self)
        submit_btn.move((width - submit_btn.size().width())/2, 410)
        submit_btn.clicked.connect(self.submit)#action in () after clicked the button
        submit_btn.setStyleSheet("""
            QPushButton {
                background-color: blue;  /* Kolor tła */
                color: white;            /* Kolor tekstu */
                font-size: 16px;         /* Rozmiar czcionki */
                border-radius: 10px;     /* Zaokrąglone rogi */
            }
            QPushButton:hover {
                background-color: lightblue;  /* Kolor po najechaniu myszką */
            }
        """)

        #create the quit button
        qiut_btn = QPushButton("QUIT", self)
        qiut_btn.move(320, 570)
        qiut_btn.clicked.connect(QApplication.instance().quit)#action in () after clicked the button
        qiut_btn.setStyleSheet("""
            QPushButton {
                background-color: blue;  /* Kolor tła */
                color: white;            /* Kolor tekstu */
                font-size: 16px;         /* Rozmiar czcionki */
                border-radius: 10px;     /* Zaokrąglone rogi */
            }
            QPushButton:hover {
                background-color: lightblue;  /* Kolor po najechaniu myszką */
            }
        """)

        self.setFixedSize(width, 600)
        self.setWindowTitle("okienko")
        self.setStyleSheet('background-color: black; color: white;')#style of window, background-color and color text
        self.setWindowIcon(QIcon('C:/Users/Sebastian/Desktop/druk/img/icons8-account-30.png'))#set an icon app

        self.show()

    #this method print in terminal text from textbox
    def submit(slef):
        print(slef.login_line_edit.text())

    #method to close the window
    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "Chcesz zamknać",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#create message box
        
        #check what an user clicked
        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication([])

login_window = LoginWindow()

app.exec()