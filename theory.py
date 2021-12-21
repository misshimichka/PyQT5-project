# экран "Теория"

from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QFont, QPixmap


class Theory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: white")
        self.setGeometry(300, 200, 1000, 600)
        self.setWindowTitle('Теория')

        self.label1 = QLabel('Сложение (2):', self)
        self.label1.move(20, 15)
        self.label1.resize(200, 30)
        self.label1.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap1 = QPixmap('images/sum_bin.png')
        self.im1 = QLabel(self)
        self.im1.move(20, 50)
        self.im1.resize(200, 200)
        self.im1.setPixmap(self.pixmap1)

        self.label2 = QLabel('Вычитание (2):', self)
        self.label2.move(250, 15)
        self.label2.resize(200, 30)
        self.label2.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap2 = QPixmap('images/min_bin.png')
        self.im2 = QLabel(self)
        self.im2.move(250, 65)
        self.im2.resize(200, 200)
        self.im2.setPixmap(self.pixmap2)

        self.label3 = QLabel('Умножение (2):', self)
        self.label3.move(500, 15)
        self.label3.resize(200, 30)
        self.label3.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap3 = QPixmap('images/mul_bin.png')
        self.im3 = QLabel(self)
        self.im3.move(500, 50)
        self.im3.resize(250, 250)
        self.im3.setPixmap(self.pixmap3)

        self.label4 = QLabel('Сложение (8):', self)
        self.label4.move(20, 300)
        self.label4.resize(200, 30)
        self.label4.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap4 = QPixmap('images/sum_oct.png')
        self.im4 = QLabel(self)
        self.im4.move(20, 350)
        self.im4.resize(200, 200)
        self.im4.setPixmap(self.pixmap4)

        self.label4 = QLabel('Вычитание (8):', self)
        self.label4.move(250, 300)
        self.label4.resize(200, 30)
        self.label4.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap5 = QPixmap('images/min_oct.png')
        self.im5 = QLabel(self)
        self.im5.move(250, 360)
        self.im5.resize(200, 200)
        self.im5.setPixmap(self.pixmap5)

        self.label4 = QLabel('Сложение (16):', self)
        self.label4.move(450, 300)
        self.label4.resize(200, 30)
        self.label4.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap6 = QPixmap('images/sum_hex.png')
        self.im6 = QLabel(self)
        self.im6.move(450, 355)
        self.im6.resize(200, 200)
        self.im6.setPixmap(self.pixmap6)

        self.label4 = QLabel('Вычитание (16):', self)
        self.label4.move(650, 300)
        self.label4.resize(200, 30)
        self.label4.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap7 = QPixmap('images/min_hex.png')
        self.im7 = QLabel(self)
        self.im7.move(650, 370)
        self.im7.resize(200, 200)
        self.im7.setPixmap(self.pixmap7)

        self.return_btn = QPushButton('Вернуться на главный экран', self)
        self.return_btn.resize(400, 30)
        self.return_btn.move(260, 560)

        self.return_btn.clicked.connect(self.stop)

    def stop(self):  # выход из экрана "Теория"
        self.close()
