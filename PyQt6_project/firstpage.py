import sys
import secondpage
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QMessageBox


class MyGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = secondpage.SecondPage()
        self.setWindowIcon(QtGui.QIcon('1054109.png'))
        self.label = QLabel("<center> Вход/Регистрация </center>")
        # self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.emailForm = QtWidgets.QLineEdit()
        self.emailForm.setPlaceholderText('Enter your email')
        # self.emailForm.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.passwordForm = QtWidgets.QLineEdit()
        self.passwordForm.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.passwordForm.setPlaceholderText('Enter your password')

        self.btn = QtWidgets.QPushButton("Продолжить")
        self.btn.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn.clicked.connect(self.show_second_window)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.emailForm)
        self.vbox.addWidget(self.passwordForm)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)

    def show_second_window(self, checked):
        # if self.w is None:
        #     self.w = secondpage.SecondPage()
        #
        #
        self.w.setWindowTitle('Заметки')
        self.w.resize(400, 400)
        self.w.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение', 'Вы уверены?',
                                     QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            for widget in QApplication.topLevelWidgets():
                if isinstance(widget, secondpage.SecondPage):
                    widget.close()

            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyGUI()
    window.setWindowTitle("Registration")
    window.resize(500, 400)
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window.show()

    app.exec()
