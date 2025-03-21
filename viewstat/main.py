from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *
import datetime
import add_new, add_ex

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()


    def setup(self):

        # date for view statistics
        end_date = datetime.date(2025, 3, 22)
        today = datetime.date.today()

        #menu
        addEX_btn = QPushButton("Add Exists Teams", self)
        addEX_btn.setFixedSize(200, 50)
        addEX_btn.move(400, 50)
        addEX_btn.clicked.connect(self.open_add_exist) # open file to insert exist

        addNew_btn = QPushButton("Add New Teams", self)
        addNew_btn.setFixedSize(200, 50)
        addNew_btn.move(400, 100)
        addNew_btn.clicked.connect(self.open_add_new) # open file to insert datas

        viewStats_btn = QPushButton("See stats", self)
        viewStats_btn.setFixedSize(200, 50)
        viewStats_btn.move(400, 150)
        # checking date
        if(today == end_date):
             viewStats_btn.show()
        else:
             viewStats_btn.hide()  

        #close button
        close_btn = QPushButton("Close", self)
        close_btn.setFixedSize(200, 50)
        close_btn.move(400, 250)
        close_btn.clicked.connect(QApplication.instance().quit)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

        self.show()

    # close app event
    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "Do you want to close app",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#create message box
        
        #check what an user clicked
        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def open_add_new(self):
            self.add_window = add_new.Add_New(self)
            self.add_window.show()
            self.hide()

    def open_add_exist(self):
            self.add_window = add_ex.Add_Exist(self)
            self.add_window.show()
            self.hide()



if __name__ == "__main__":
    app = QApplication([])

program = Program()

app.exec()