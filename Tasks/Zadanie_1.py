#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите простейший калькулятор, состоящий из двух текстовых полей, куда пользователь вводит числа, и четырех кнопок
"+", "-", "*", "/". Результат вычисления должен отображаться в метке. Если арифметическое действие выполнить невозможно
(например, если были введены буквы, а не числа), то в метке должно появляться слово "ошибка".
"""

import sys
from PySide2.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QApplication, QLabel
from PySide2.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label_1 = QLabel("Введите числа")
        self.label_1.setFont(QFont('Arial', 13))
        self.label_2 = QLabel("Результат операции:")
        self.line_1 = QLineEdit(self)
        self.line_2 = QLineEdit(self)
        self.butn1 = QPushButton("+", self)
        self.butn2 = QPushButton("-", self)
        self.butn3 = QPushButton("*", self)
        self.butn4 = QPushButton("/", self)
        self.initialization()

    def initialization(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle("Задание 1. Калькулятор")
        self.displayWidgets()

    def displayWidgets(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.label_1)
        v_box.addWidget(self.line_1)
        v_box.addWidget(self.line_2)
        v_box.addWidget(self.butn1)
        v_box.addWidget(self.butn2)
        v_box.addWidget(self.butn3)
        v_box.addWidget(self.butn4)
        v_box.addWidget(self.label_2)
        self.setLayout(v_box)
        self.butn1.clicked.connect(self.Addition)
        self.butn2.clicked.connect(self.Subtraction)
        self.butn3.clicked.connect(self.Multiplication)
        self.butn4.clicked.connect(self.Division)

    def Addition(self):
        try:
            number_1 = self.line_1.text()
            number_2 = self.line_2.text()
            summa = str(float(number_1) + float(number_2))
            self.label_2.setText(summa)
        except ValueError:
            self.label_2.setText("Ошибка")

    def Subtraction(self):
        try:
            number_1 = self.line_1.text()
            number_2 = self.line_2.text()
            sub = str(float(number_1) - float(number_2))
            self.label_2.setText(sub)
        except ValueError:
            self.label_2.setText("Ошибка")

    def Division(self):
        try:
            number_1 = self.line_1.text()
            number_2 = self.line_2.text()
            div = str(float(number_1) / float(number_2))
            self.label_2.setText(div)
        except ValueError:
            self.label_2.setText("Ошибка")
        except ZeroDivisionError:
            self.label_2.setText("Деление на 0")

    def Multiplication(self):
        try:
            number_1 = self.line_1.text()
            number_2 = self.line_2.text()
            mul = str(float(number_1) * float(number_2))
            self.label_2.setText(mul)
        except ValueError:
            self.label_2.setText("Ошибка")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
