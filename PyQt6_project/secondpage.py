import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QPushButton, QToolBar, QMenuBar, QMenu, \
    QMainWindow


class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1054109.png'))
        self.label = QLabel('<center>Здесь пока ничего нет</center>')
        self.button = QPushButton('Закрыть это окно')
        self.button.clicked.connect(self.close_window)
        self.box = QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

        self.menubar = QMenuBar()
        self.fileMenu = QMenu("&File")
        self.edit = QMenu('&Edit')
        self.menubar.addMenu(self.fileMenu)
        self.menubar.addMenu(self.edit)
        self.fileMenu.addAction('Hello', lambda: print('Hello'))
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('Hello', lambda: print('Hello'))
        self.edit.addAction('Hello', lambda: print('Hello'))
        self.box.setMenuBar(self.menubar)


    def close_window(self):
        self.close()
