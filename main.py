# главный экран проекта

from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from training import Train
from testing import *
from theory import Theory
from press_f import PressF
from error_name import Error

SCREEN_SIZE = [1000, 600]


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, *SCREEN_SIZE)
        self.setWindowTitle('Тренажер "Системы счисления"')

        self.pixmap = QPixmap('images/numbers.png')
        self.image = QLabel(self)
        self.image.move(375, 150)
        self.image.resize(256, 256)
        self.image.setPixmap(self.pixmap)

        self.train_btn = QPushButton('Начать тренировку', self)
        self.train_btn.resize(200, 40)
        self.train_btn.move(150, 450)

        self.test_btn = QPushButton('Начать тест', self)
        self.test_btn.resize(200, 40)
        self.test_btn.move(650, 450)

        self.theory_btn = QPushButton('Теория', self)
        self.theory_btn.resize(200, 40)
        self.theory_btn.move(400, 450)

        self.hello_label = QLabel(self)
        self.hello_label.move(210, 80)
        self.hello_label.setText('Программа-тренажер "Системы счисления"')
        self.hello_label.setFont(QFont("Times", 20, QFont.Bold))

        self.f_label = QLabel(self)
        self.f_label.move(300, 530)
        self.f_label.setText('!PRESS "F" TO PAY RESPECT!')
        self.f_label.setFont(QFont("Times", 20, QFont.Bold))

        self.train_btn.clicked.connect(self.begin_train)
        self.test_btn.clicked.connect(self.begin_testing)
        self.theory_btn.clicked.connect(self.theory)

    def begin_train(self):  # вызов функции, отвечающей за открытие экрана "Тренировка"
        self.train_form = Train(self, 'Тренировка "Системы счисления"')
        self.train_form.show()

    def begin_testing(self):  # вызов функции, отвечающей за открытие экрана "Тест"
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Имя Фамилия")
        if ok_pressed:
            if name == '':
                self.error = Error()  # вызов экрана "Ошибка" при неверном вводе пользователя
                self.error.show()
            else:
                self.test_form = Test(self, name)
                self.test_form.show()

    def theory(self):   # вызов функции, отвечающей за открытие экрана "Теория"
        self.theory = Theory()
        self.theory.show()

    def keyPressEvent(self, event):   # вызов функции, отвечающей за открытие экрана с контактной информацией
        if event.key() == Qt.Key_F:
            self.press_f = PressF()
            self.press_f.show()


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = Main()
    ex.setObjectName("MainWindow")
    ex.setStyleSheet("#MainWindow{background-color:cyan}")
    ex.show()
    sys.exit(app.exec())
