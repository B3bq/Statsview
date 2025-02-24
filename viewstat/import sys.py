import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rozwijana lista wyboru")
        self.setGeometry(100, 100, 400, 200)

        # Główne okno centralne
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tworzymy rozwijaną listę (QComboBox)
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Opcja 1", "Opcja 2", "Opcja 3", "Opcja 4"])  # Dodajemy opcje

        # Etykieta do wyświetlania wybranej opcji
        self.label = QLabel("Wybierz opcję z listy:")
        self.label.setStyleSheet("font-size: 16px;")

        # Połączenie sygnału zmiany wyboru z funkcją
        self.combo_box.currentIndexChanged.connect(self.update_label)

        # Układ (layout) do rozmieszczenia widżetów
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)

        # Ustawienie układu dla centralnego widżetu
        central_widget.setLayout(layout)

    def update_label(self, index):
        """Aktualizuje etykietę po zmianie wyboru."""
        selected_text = self.combo_box.itemText(index)
        self.label.setText(f"Wybrano: {selected_text}")


# Główna funkcja
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
