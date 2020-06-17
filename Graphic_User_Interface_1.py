import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

Text = ""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(448, 300)

        label1 = QLabel("""QLabel은 텍스트를 넣어준다 메모
QLineEdit 은 텍스트를 바꾼다 메모
QPushButton은 버튼을 누른다 메모""", self)
        label1.setAlignment(Qt.AlignCenter)
        label1.move(280, 10)

        qle = QLineEdit(self)
        qle.move(408, 300)
        qle.textChanged[str].connect(self.onChanged)


        btn = QPushButton('Enter', self)
        btn.move(448, 400)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('MAP')
        self.setWindowIcon(QIcon('map.png'))
        self.resize(960, 540)
        self.show()

    def onChanged(self, text):
        global Text
        self.lbl.setText(text)
        self.lbl.adjustSize()
        Text = text

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()
