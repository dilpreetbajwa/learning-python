"""
GUI line edits
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 50)
        self.button.setGeometry(220, 10, 200, 50)
        self.line_edit.setStyleSheet("font-size: 20px;" "font-family: Arial;")
        self.button.setStyleSheet("font-size: 20px;" "font-family: Arial;")

        self.line_edit.setPlaceholderText("Enter your name")

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print(f"Hello, {self.line_edit.text()}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
