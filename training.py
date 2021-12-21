# экран "Тренировка"

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QTextBrowser
from PyQt5.QtGui import QFont, QPixmap
from operation import *


class Train(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 200, 1000, 600)
        self.setWindowTitle('Тренировка')

        self.task_btn = QPushButton('Новое задание', self)
        self.task_btn.resize(300, 50)
        self.task_btn.move(320, 450)

        self.return_btn = QPushButton('Вернуться на главный экран', self)
        self.return_btn.resize(400, 30)
        self.return_btn.move(260, 560)

        self.task_label = QLabel(args[-1], self)
        self.task_label.move(310, 50)
        self.task_label.setFont(QFont("Times", 15, QFont.Bold))

        self.num_input = QLineEdit(self)
        self.num_input.resize(150, 20)
        self.num_input.move(400, 410)

        self.textBrowser = QTextBrowser(self)
        self.textBrowser.resize(150, 100)
        self.textBrowser.move(400, 300)

        self.strings, self.evals = operations()
        self.ind = randint(0, 6)
        self.textBrowser.setText(self.strings[self.ind])

        self.pixmap1 = QPixmap('images/right_picture.jpg')
        self.im1 = QLabel(self)
        self.im1.move(370, 90)
        self.im1.resize(250, 200)
        self.im1.setPixmap(self.pixmap1)

        self.task_btn.clicked.connect(self.begin)
        self.return_btn.clicked.connect(self.stop)

    def begin(self):
        self.num = self.num_input.text().upper()
        if self.num == self.evals[self.ind][2:].upper():
            self.task_label.setText('Верно!')
            self.setStyleSheet("background-color:honeydew")
            self.task_label.move(440, 50)
            self.pixmap1 = QPixmap('images/right_picture.jpg')
            self.im1.setPixmap(self.pixmap1)
        else:
            self.task_label.setText('Неверно!')
            self.setStyleSheet("background-color:mistyrose")
            self.task_label.move(420, 50)
            self.pixmap1 = QPixmap('images/wrong_picture.png')
            self.im1.setPixmap(self.pixmap1)
        self.num_input.clear()
        self.strings, self.evals = operations()
        self.ind = randint(0, 6)
        self.textBrowser.setText(self.strings[self.ind])

    def stop(self):  # выход из экрана "Теория"
        self.close()
