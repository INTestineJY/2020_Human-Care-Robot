import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt

html_dict = {'033': "gangwon_map.html", '031': "gyeonggi_map.html",
             '043': "chungbuk_map.html", '041': "chungnam_map.html",
             '063': "jeonbuk_map.html", '054': "gyeongbuk_map.html",
             '055': "gyeongnam_map.html", '061': "jeonnam_map.html",
             '02': "seoul_map.html", '044': "sejong_map.html",
             '051': "busan_map.html", '052': "ulsan_map.html",
             '032': "incheon_map.html", '042': "daejeon_map.html",
             '053': "daegu_map.html", '062': "gwangju_map.html",
             '064': "jeju_map.html"}

Text = ""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(448, 300)

        label1 = QLabel("""서울 : 02
        경기 : 031     인천 : 032     강원 : 033
        충남 : 041     대전 : 042     충북 : 043     세종 : 044
        부산 : 051     울산 : 052     대구 : 053     경북 : 054     경남 : 055
        전남 : 061     광주 : 062     전북 : 063     제주 : 064""", self)
        label1.setAlignment(Qt.AlignCenter)
        label1.move(280, 10)

        label2 = QLabel("""위의 지역번호 중 원하는 지역의 번호를 입력하세요😎""", self)
        label2.setAlignment(Qt.AlignCenter)
        label2.move(350,250)

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



