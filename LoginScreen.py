from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy, QLineEdit, QFormLayout, QDialog, QTextBrowser, QMessageBox, \
    QListWidgetItem, QHBoxLayout, QAbstractItemView, QListWidget
from PyQt5.QtCore import Qt, QEvent, QPoint
import sqlite3

from CoffeeShop import CoffeeShop
from ForgotPass import ForgotPass
from SignUpScreen import SignUpScreen
from Spotify import SpotifyPlaylistWidget


class LoginScreen(QWidget):
    def __init__(self, open_main_app_callback=None):
        super().__init__()



        # Window
        self.setWindowTitle("Coffee Shop Login")
        self.setGeometry(800, 300, 400, 500)
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #00000;")

        # Logo
        logo_label = QLabel(self)
        logo_label.setStyleSheet("min-width: 300px;"
                                 "min-height: 200px;"
                                 "background-image: url('img/logo.png');"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;"
                                 "background-size: cover;")

        self.username_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)

        # Fonts
        login_font = QFont()
        login_font.setBold(True)
        login_font.setPointSize(20)

        small_font = QFont()
        small_font.setPointSize(8)

        # Layouts
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Kullanıcı Girişi", font=login_font))
        form_layout.setSpacing(120)
        form_layout.addRow("Username:", self.username_edit)
        form_layout.addRow("Password:", self.password_edit)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.login_button)
        form_layout.setSpacing(20)


        # forgot pass
        forgot_pass_button = QPushButton("Forgot Password", self)
        forgot_pass_button.clicked.connect(self.open_forgot_pass_screen)
        button_layout.addWidget(forgot_pass_button)

        # sign up
        signup_button = QPushButton("Yeni Üye", self)
        signup_button.clicked.connect(self.open_signup_screen)
        button_layout.addWidget(signup_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        # Connect login button click event to a function
        self.login_button.clicked.connect(self.authenticate_user)
        self.login_button.clicked.connect(self.open_main_app)
        self.open_main_app_callback = open_main_app_callback


    def open_forgot_pass_screen(self):
        forgot_pass_screen = ForgotPass()
        forgot_pass_screen.exec_()
    def open_signup_screen(self):
        signup_screen = SignUpScreen()
        signup_screen.exec_()

    def open_forget_pass_screen(self):
        # Implement the logic to open the "Şifremi Unuttum" screen
        print("Şifremi Unuttum screen will be opened.")


    def conn(self):
        conn = sqlite3.connect('db/coffee_shop.db')
        cursor = conn.cursor()
        return conn, cursor

    def authenticate_user(self):
        try:
            username = self.username_edit.text()
            password = self.password_edit.text()

            conn, cursor = self.conn()
            cursor.execute('SELECT * FROM admins WHERE admin_username = ? AND admin_pass = ?', (username, password))
            admin_data = cursor.fetchone()
            conn.close()

            if admin_data:
                self.open_main_app(admin=True)
            else:
                conn, cursor = self.conn()
                cursor.execute('SELECT * FROM customers WHERE username = ? AND pass = ?', (username, password))
                customer_data = cursor.fetchone()
                conn.close()

                if customer_data:
                    self.open_main_app(admin=False)
                else:
                    print("Invalid credentials")
        except Exception as e:
            print(f"An error occurred: {e}")

    def open_main_app(self, admin=False):
        if admin:
            self.close()
            self.open_main_app_callback(admin=True, main_app=self)  # Pass main_app as an argument

        else:
            #customer page
            print("Customer logged in, opening customer version of the app")
def open_main_app(admin=False, main_app=None):
    try:
        coffee_shop = CoffeeShop()
        spotifyPlaylistWidget=SpotifyPlaylistWidget()

        SpotifyPlaylistWidget.setParent(coffee_shop)

        coffee_shop.show()
        SpotifyPlaylistWidget.show()

        main_app.close()
    except Exception as e:
        print(f"An error occurred while opening the main app: {e}")

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_app = LoginScreen(open_main_app_callback=open_main_app)
    main_app.show()

    sys.exit(app.exec_())