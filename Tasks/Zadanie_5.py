#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
индикатор которых выключен. Если какая-нибудь кнопка включается, то в
метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
не должно
"""

import sys
from PySide2.QtWidgets import QWidget, QButtonGroup, QApplication, QPushButton, QGridLayout, QLabel
from PySide2.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label_1 = QLabel(self)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.group = QButtonGroup()
        self.radio_1 = QPushButton('СКФУ')
        self.radio_2 = QPushButton('МИРЭА')
        self.radio_3 = QPushButton('СтГАУ')
        self.initialization()

    def initialization(self):
        self.setGeometry(200, 200, 350, 200)
        self.setWindowTitle("Задание 5")
        self.displayWidgets()

    def displayWidgets(self):
        self.radio_1.setCheckable(True)
        self.radio_2.setCheckable(True)
        self.radio_3.setCheckable(True)
        self.group.addButton(self.radio_1)
        self.group.addButton(self.radio_2)
        self.group.addButton(self.radio_3)
        self.group.buttonClicked.connect(self.clicked_button)
        grid = QGridLayout()
        grid.setSpacing(12)
        grid.addWidget(self.radio_1, 1, 0)
        grid.addWidget(self.radio_2, 2, 0)
        grid.addWidget(self.radio_3, 3, 0)
        grid.addWidget(self.label_1, 2, 2)
        self.setLayout(grid)

    def clicked_button(self, butn):
        institutes = {
            'СКФУ': 'Вы поступили в СКФУ',
            'МИРЭА': 'Вы поступили в МИРЭА',
            'СтГАУ': 'Вы поступили в СтГАУ'}
        self.label_1.setText(institutes[butn.text()])


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
