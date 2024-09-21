"""
GUI
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(0, 0, 500, 500)

        label = QLabel("Hello World", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet(
            "color: white;"
            "background-color: black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        imageLabel = QLabel(self)
        imageLabel.setGeometry(0, 150, 300, 300)

        pixmap = QPixmap("logo.png")
        imageLabel.setPixmap(pixmap)
        imageLabel.setScaledContents(True)

        imageLabel.setGeometry(
            (self.width() - imageLabel.width()) // 2,
            (self.height() - imageLabel.height()) // 2 + 50,
            imageLabel.width(),
            imageLabel.height(),
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
