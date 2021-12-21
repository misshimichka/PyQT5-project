# экран для связи с разработчиком

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
SCREEN_SIZE = [1000, 600]


class PressF(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, *SCREEN_SIZE)
        self.setWindowTitle('Press F to pay respect to misshimichka')

        self.task_label = QLabel('Если Вам понравилось это приложение, или Вы хотите оставить свои отзывы\n'
                                 'и предложения, напишите на почту chegodaeva.stacy@gmail.com. \n'
                                 'Я с удовольствием прочитаю Ваши пожелания и постараюсь воплотить их. \n'
                                 'А также подписывайтесь на мой аккаунт в Instagram @misshimichka :)', self)
        self.task_label.move(50, 100)
        self.task_label.resize(900, 100)
        self.task_label.setFont(QFont("Times", 14, QFont.Bold))

        self.pixmap = QPixmap('images/rate_us.jpg')
        self.image = QLabel(self)
        self.image.move(300, 230)
        self.image.resize(423, 240)
        self.image.setPixmap(self.pixmap)

        self.return_btn = QPushButton('Вернуться на главный экран', self)
        self.return_btn.resize(400, 30)
        self.return_btn.move(300, 560)

        self.return_btn.clicked.connect(self.stop)

    def stop(self):  # выход из экрана "Теория"
        self.close()
