#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок "Открыть" и "Сохранить".
При клике на первую должен открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
должно загружаться в поле типа Text .
При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен сохраняться в файле под именем,
которое пользователь указал в однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
"""

import sys
from PySide2.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QTextEdit, \
    QHBoxLayout, QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.line_1 = QLineEdit(self)
        self.label_1 = QTextEdit(self)
        self.butn1 = QPushButton("Открыть файл", self)
        self.butn2 = QPushButton("Сохранить файл", self)
        self.initialization()

    def initialization(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Задание 4")
        self.display_widgets()

    def display_widgets(self):
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        v_box.addLayout(h_box)
        self.butn1.clicked.connect(self.make_open)
        self.butn2.clicked.connect(self.make_save)
        h_box.addWidget(self.line_1)
        h_box.addWidget(self.butn1)
        h_box.addWidget(self.butn2)
        v_box.addWidget(self.label_1)
        self.setLayout(v_box)

    def make_save(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Save File As',
            '',
            "Text Files (*.txt)"
        )
        if filename:
            text = self.label_1.toPlainText()
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(text)

    def make_open(self):
        if self.line_1.text() == '':
            file_name = QFileDialog.getOpenFileName(self)
            with open(file_name[0], 'r', encoding="utf-8") as f:
                location = f.read()
            self.label_1.setText(location)
        else:
            try:
                file_name = self.line_1.text()
                with open(file_name, 'r', encoding="utf-8") as f:
                    location = f.read()
                self.label_1.setText(location)
            except ValueError:
                self.label_1.setText(f"Файл не найден")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
