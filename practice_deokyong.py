import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        boxy = QGridLayout()
        boxy.addWidget(self.btn1, 0, 0)
        boxy.addWidget(self.btn2, 0, 1)
        boxy.addWidget(self.btn3, 1, 0)

        # self.setLayout(vbox)
        self.setLayout(boxy)
        self.setWindowTitle('QPushButton')
        self.setGeometry(100, 100, 1080, 720)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
