from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy, QLineEdit, QFormLayout, QDialog, QTextBrowser, QMessageBox, \
    QListWidgetItem, QHBoxLayout, QAbstractItemView, QListWidget
from PyQt5.QtCore import Qt, QEvent
import sqlite3

class ForgotPass(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Forgot Password")
        self.setGeometry(800, 300, 400, 200)

        layout = QVBoxLayout(self)

        self.email_edit = QLineEdit(self)
        self.reset_button = QPushButton("Reset Password", self)

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_edit)
        layout.addWidget(self.reset_button)

        self.reset_button.clicked.connect(self.perform_reset)

    def perform_reset(self):
        # Implement the logic for resetting the password (e.g., sending an email)
        email = self.email_edit.text()
        QMessageBox.information(self, "Password Reset", f"Password reset instructions sent to {email}")