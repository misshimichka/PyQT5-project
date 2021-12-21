# экран "Тест"

from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QTextBrowser, QMainWindow
from PyQt5.QtGui import QFont
from operation import *
from results import Result
import sqlite3
import sys


def excepthook(exc_type, exc_value, exc_tb):  # проверка на наличие ошибок в работе виджета PyQT
    sys.__excepthook__(exc_type, exc_value, exc_tb)


class Test(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.name = args[-1]

        self.f = open('mistakes.txt', mode='wt', encoding='utf-8')

        self.score = 0
        self.tasks = 0
        self.setGeometry(300, 200, 1000, 600)
        self.setWindowTitle('Тест')

        con = sqlite3.connect('db_PyQt.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM students WHERE name=?",
                             (self.name,)).fetchall()
        if not result:
            self.label = QLabel('Здравствуйте! \nУ Вас нет предыдущих результатов', self)
            self.label.move(300, 150)
            self.label.resize(400, 50)
            self.label.setFont(QFont("Times", 15, QFont.Bold))
        else:
            text = f'Здравствуйте!\n' \
                   f'Ваш предыдущий тезультат:\n' \
                   f'{result[0][2]} из 15'
            self.label = QLabel(text, self)
            self.label.move(300, 150)
            self.label.resize(400, 100)
            self.label.setFont(QFont("Times", 13, QFont.Bold))

        self.task_btn = QPushButton('Новое задание', self)
        self.task_btn.resize(300, 50)
        self.task_btn.move(320, 450)

        self.task_label = QLabel('Задание №1', self)
        self.task_label.move(400, 100)
        self.task_label.resize(400, 50)
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

        self.task_btn.clicked.connect(self.begin)

    def begin(self):
        self.num = self.num_input.text()
        if self.num == self.evals[self.ind][2:].upper():
            self.score += 1
        else:
            x = f'{self.strings[self.ind]}{self.evals[self.ind][2:]}, your answer: {self.num}\n'
            self.f.write(x)
        self.tasks += 1
        self.task_label.setText(f'Задание №{self.tasks + 1}')
        self.task_label.move(400, 100)
        if self.tasks == 15:
            x = int((self.score / self.tasks) * 100)
            if x <= 20:
                mark = 1
            elif 20 < x <= 40:
                mark = 2
            elif 40 < x <= 60:
                mark = 3
            elif 60 < x <= 80:
                mark = 4
            else:
                mark = 5
            con = sqlite3.connect('db_PyQt.db')
            cur = con.cursor()
            result = cur.execute("SELECT * FROM students WHERE name=?",
                                 (self.name,)).fetchall()
            if not result:
                cur.execute('INSERT INTO students(score,name, mark,tasks) VALUES(?,?,?,15)',
                            (str(self.score), self.name, mark))
                con.commit()
            else:
                cur.execute('UPDATE students SET score=?, mark=? WHERE name=?',
                            (str(self.score), mark, self.name))
                con.commit()
            self.f.close()
            self.close()
            self.result = Result(self, [mark, self.score])  # запуск экрана "Результаты"
            self.result.show()
        self.num_input.clear()
        self.strings, self.evals = operations()
        self.ind = randint(0, 6)
        self.textBrowser.setText(self.strings[self.ind])
