from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy, QLineEdit, QFormLayout, QDialog, QTextBrowser, QMessageBox, \
    QListWidgetItem, QHBoxLayout, QAbstractItemView, QListWidget
from PyQt5.QtCore import Qt, QEvent
import sqlite3

class SignUpScreen(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign Up")
        self.setGeometry(800, 300, 400, 200)

        layout = QVBoxLayout(self)

        self.name_edit = QLineEdit(self)
        self.surname_edit = QLineEdit(self)
        self.email_edit = QLineEdit(self)
        self.pass_edit = QLineEdit(self)
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.pass_rpt_edit = QLineEdit(self)
        self.pass_rpt_edit.setEchoMode(QLineEdit.Password)
        self.signup_button = QPushButton("Sign Up", self)


        layout.addWidget(QLabel("İsim:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Soyisim:"))
        layout.addWidget(self.surname_edit)
        layout.addWidget(QLabel("email:"))
        layout.addWidget(self.email_edit)
        layout.addWidget(QLabel("Şifre:"))
        layout.addWidget(self.pass_edit)
        layout.addWidget(QLabel("Şifre Tekrar Girin:"))
        layout.addWidget(self.pass_rpt_edit)


        layout.addWidget(self.signup_button)

        self.signup_button.clicked.connect(self.signup)

    def signup(self):
        username = self.name_edit.text()
        password = self.pass_edit.text()
        password_repeat = self.pass_rpt_edit.text()

        if password != password_repeat:
            QMessageBox.critical(self, "Error", "Şifreler uyuşmuyor. Lütfen tekrar kontrol edin.")
            return

        # If the passwords match, you can proceed with the signup logic
        print(f"Signed up: Username - {username}, Password - {password}")
