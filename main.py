from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy, QLineEdit, QFormLayout, QDialog, QTextBrowser, QMessageBox, \
    QListWidgetItem, QHBoxLayout, QAbstractItemView, QListWidget
from PyQt5.QtCore import Qt, QEvent
import sqlite3
from PyQt5.QtWidgets import QApplication
from LoginScreen import open_main_app, LoginScreen

if __name__ == "__main__":
    app = QApplication([])
    main_app = LoginScreen(open_main_app_callback=open_main_app)
    main_app.show()
    app.exec()






