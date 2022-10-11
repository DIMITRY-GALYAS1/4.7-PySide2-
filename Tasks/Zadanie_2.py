#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги.
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый, #00ff00 – зеленый,
#007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
"""

import sys
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label_1 = QLabel(self)
        self.line_1 = QLineEdit(self)
        self.butn1 = QPushButton(self)
        self.butn2 = QPushButton(self)
        self.butn3 = QPushButton(self)
        self.butn4 = QPushButton(self)
        self.butn5 = QPushButton(self)
        self.butn6 = QPushButton(self)
        self.butn7 = QPushButton(self)
        self.initialization()

    def initialization(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle("Задание 2. Выбор цвета")
        self.display_widgets()

    def display_widgets(self):
        self.butn1.setStyleSheet("background-color: #ff0000;")
        self.butn1.clicked.connect(self.make_red)
        self.butn2.setStyleSheet("background-color: #ff7d00;")
        self.butn2.clicked.connect(self.make_orange)
        self.butn3.setStyleSheet("background-color: #ffff00;")
        self.butn3.clicked.connect(self.make_yellow)
        self.butn4.setStyleSheet("background-color: #00ff00;")
        self.butn4.clicked.connect(self.make_green)
        self.butn5.setStyleSheet("background-color: #007dff;")
        self.butn5.clicked.connect(self.make_cyan)
        self.butn6.setStyleSheet("background-color: #0000ff;")
        self.butn6.clicked.connect(self.make_blue)
        self.butn7.setStyleSheet("background-color: #7d00ff;")
        self.butn7.clicked.connect(self.make_purple)

        v_box = QVBoxLayout()
        v_box.addWidget(self.label_1)
        v_box.addWidget(self.line_1)
        v_box.addWidget(self.butn1)
        v_box.addWidget(self.butn2)
        v_box.addWidget(self.butn3)
        v_box.addWidget(self.butn4)
        v_box.addWidget(self.butn5)
        v_box.addWidget(self.butn6)
        v_box.addWidget(self.butn7)
        self.setLayout(v_box)

    def make_red(self):
        self.label_1.setText("Красный")
        self.line_1.setText("#ff0000")

    def make_orange(self):
        self.label_1.setText("Оранжевый")
        self.line_1.setText("#ff7d00")

    def make_yellow(self):
        self.label_1.setText("Желтый")
        self.line_1.setText("#ffff00")

    def make_green(self):
        self.label_1.setText("Зеленый")
        self.line_1.setText("#00ff00")

    def make_cyan(self):
        self.label_1.setText("Голубой")
        self.line_1.setText("#007dff")

    def make_blue(self):
        self.label_1.setText("Синий")
        self.line_1.setText("#0000ff")

    def make_purple(self):
        self.label_1.setText("Фиолетовый")
        self.line_1.setText("#7d00ff")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
