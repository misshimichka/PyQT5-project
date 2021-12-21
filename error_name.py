# экран "Ошибка"

from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QFont, QPixmap


class Error(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: white")
        self.setGeometry(300, 200, 1000, 600)
        self.setWindowTitle('Ошибка')

        self.text = f'Вы ввели пустое значение в диалоговом окне! \n' \
                    f'Убедительно просим Вас пройти тест еще раз ' \
                    f'с корректно введенными \n' \
                    f'данными'

        self.label1 = QLabel(self.text, self)
        self.label1.move(100, 15)
        self.label1.resize(800, 100)
        self.label1.setFont(QFont("Times", 15, QFont.Bold))

        self.pixmap1 = QPixmap('images/wrong_picture.png')
        self.im1 = QLabel(self)
        self.im1.move(370, 150)
        self.im1.resize(250, 200)
        self.im1.setPixmap(self.pixmap1)

        self.setStyleSheet("background-color:mistyrose")

        self.return_btn = QPushButton('Вернуться на главный экран', self)
        self.return_btn.resize(400, 30)
        self.return_btn.move(260, 560)

        self.return_btn.clicked.connect(self.stop)

    def stop(self):  # выход из экрана "Теория"
        self.close()
