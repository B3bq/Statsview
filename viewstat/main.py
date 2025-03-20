from PySide6.QtGui import QPixmap, QCloseEvent, QIcon
from PySide6.QtWidgets import *
import add_new

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()


    def setup(self):

        #menu
        addEX_btn = QPushButton("Add Exists Teams", self)
        addEX_btn.setFixedSize(200, 50)
        addEX_btn.move(400, 50)

        addNew_btn = QPushButton("Add New Teams", self)
        addNew_btn.setFixedSize(200, 50)
        addNew_btn.move(400, 100)
        addNew_btn.clicked.connect(self.open_add_new)

        viewStats_btn = QPushButton("See stats", self)
        viewStats_btn.setFixedSize(200, 50)
        viewStats_btn.move(400, 150)        

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")

        self.show()

    def open_add_new(self):
            self.add_window = add_new.Program()
            self.add_window.show()
            self.close()




if __name__ == "__main__":
    app = QApplication([])

program = Program()

app.exec()