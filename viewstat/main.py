from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import *
from translator import Translator
import add_new, add_ex, summary_window, main_window, sys, os, json


class Program(QMainWindow):
    def __init__(self):
        super().__init__()

        # stack to switch screens
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # language for app
        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)
        if user_data["lang"] != "":
            self.translator = Translator(user_data["lang"])
        else:
            self.translator = Translator("en")

        # widgets
        self.add_new_window = add_new.Add_New(self, self.translator)
        self.add_ex_window = add_ex.Add_Exist(self, self.translator)
        self.summary_window = summary_window.Summary(self, self.translator)
        self.main_window = main_window.Main_window(self, self.translator)

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

    def lang_change(self, lang):
        self.translator.set_language(lang)

        self.main_window.retranslate_ui()
        self.add_ex_window.retranslate_ui()
        self.add_new_window.retranslate_ui()
        self.summary_window.retranslate_ui()

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

        file_path = os.path.join(os.path.dirname(__file__), 'save.json')
        with open(file_path, 'r') as file:
            user_data = json.load(file)

        msg = QMessageBox(self)
        
        if user_data["lang"] == "en":
            msg.setWindowTitle("Close App")
            msg.setText("Do you want to close the app?")
            yes_button = msg.addButton("Yes", QMessageBox.YesRole)
            no_button = msg.addButton("No", QMessageBox.NoRole)
        else:
            msg.setWindowTitle("Zamknij")
            msg.setText("Czy chcesz zamknąć aplikację?")
            
            yes_button = msg.addButton("Tak", QMessageBox.YesRole)
            no_button = msg.addButton("Nie", QMessageBox.NoRole)
            
        msg.setDefaultButton(no_button)
        msg.exec()

        #check what an user clicked
        if msg.clickedButton() == yes_button:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
