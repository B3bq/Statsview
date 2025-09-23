from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import *
import add_new, add_ex, summary_window, main_window, sys, os


class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        # stack to switch screens
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # widgets
        self.add_new_window = add_new.Add_New(self)
        self.add_ex_window = add_ex.Add_Exist(self)
        self.summary_window = summary_window.Summary(self)
        self.main_window = main_window.Main_window(self)

        # adding widgets to stack
        self.stack.addWidget(self.main_window)
        self.stack.addWidget(self.add_ex_window)
        self.stack.addWidget(self.add_new_window)
        self.stack.addWidget(self.summary_window)

        #basic window settings
        self.setFixedSize(1000, 400)
        self.setWindowTitle("Statsview")
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "logo.svg")
        self.setWindowIcon(QIcon(icon_path))

        self.stack.setCurrentWidget(self.main_window)

    def open_main_window(self):
        self.summary_window.reset_summary()
        self.add_ex_window.reset()
        self.add_new_window.restart()
        self.stack.setCurrentWidget(self.main_window)

    def open_add_new(self):
        self.stack.setCurrentWidget(self.add_new_window)

    def open_add_exist(self):
        self.stack.setCurrentWidget(self.add_ex_window)

    def open_summary(self):
        self.stack.setCurrentWidget(self.summary_window)

    # close app event
    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "Do you want to close app",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)#create message box
        
        #check what an user clicked
        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
