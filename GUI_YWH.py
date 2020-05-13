import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        start_image = QImage("./image/start_image.png")

        voice_button = QPushButton("목소리 선택")
        usertype_button = QPushButton("사용자 유형 선택")
        purpose_button = QPushButton("사용 목적 선택")

        start_window = QVBoxLayout()
        start_window.addWidget(start_image)
        self.setLayout(start_window)
