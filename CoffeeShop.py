from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QGridLayout, \
    QStackedWidget, QScrollArea, QSizePolicy, QLineEdit, QFormLayout, QDialog, QTextBrowser, QMessageBox, \
    QListWidgetItem, QHBoxLayout, QAbstractItemView, QListWidget, QSpacerItem, QShortcut
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
import sqlite3

from CartComponents import CartComponents
from CustomerCard import CustomerCard
from ProductCard import ProductCard
from SaleCard import SaleCard
from database import connect_to_db



class CoffeeShop(QMainWindow):
    addedToCart = pyqtSignal(dict)
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Coffee Shop")
        self.showFullScreen()
        self.setStyleSheet("background-color: #00000;")
        close_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        close_shortcut.activated.connect(self.close_application)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout using grid
        main_layout = QVBoxLayout(self.centralWidget())

        # Logo
        logo_label = QLabel(self)
        logo_label.setStyleSheet("min-width: 300px;"
                                 "min-height: 200px;"
                                 "background-image: url('img/logo.png');"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;"
                                 "background-size: cover;")

        main_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        main_layout.addItem(QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        # Navbar
        self.nav_bar = QWidget(self)
        self.nav_layout = QHBoxLayout(self.nav_bar)
        self.nav_layout.setSpacing(400)
        self.nav_bar.setMinimumHeight(50)
        self.nav_bar.setStyleSheet("background-image: url('img/option_one_nav.png');"
                                   "background-size: cover 10px;"
                                   "margin: 0; padding: 0;")
        main_layout.addWidget(self.nav_bar, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # stacked_widget
        self.stacked_widget = QStackedWidget(self)

        # products_btn
        products_button = QPushButton("Products", self)
        products_button.clicked.connect(self.show_products)
        self.nav_layout.addWidget(products_button, 4, 0, 1, 2)
        products_button.setStyleSheet(
            "background-color: #000000; color: #FFFFFF; border: none; font-size: 16px; font-weight: bold;padding-bottom: 5px;")

        products_button.clicked.connect(lambda: self.change_background('img/option_one_nav.png'))

        # sales_btn
        sales_button = QPushButton("Sales", self)
        sales_button.clicked.connect(self.show_sales)
        self.nav_layout.addWidget(sales_button, 4, 1, 1, 2)
        sales_button.setStyleSheet(
            "background-color: #000000; color: #FFFFFF; border: none; font-size: 16px; font-weight: bold; padding-bottom: 5px;")
        sales_button.clicked.connect(lambda: self.change_background('img/option_two_nav.png'))

        # customers_btn
        customers_button = QPushButton("Customers", self)
        customers_button.clicked.connect(self.show_customers)
        self.nav_layout.addWidget(customers_button, 4, 2, 1, 2)
        customers_button.setStyleSheet(
            "background-color: #000000; color: #FFFFFF; border: none; font-size: 16px; font-weight: bold;padding-bottom: 5px;")
        customers_button.clicked.connect(lambda: self.change_background('img/option_three_nav.png'))

        # bottom_part
        bottom_part = QScrollArea(self)
        bottom_part.setWidgetResizable(True)
        bottom_part.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(bottom_part)
        bottom_part.setWidget(self.stacked_widget)

        # alt kısmı dinamik yapan stacked widget
        #self.stacked_widget = QStackedWidget(self)
        bottom_part.setWidget(self.stacked_widget)

        self.init_products_view()
        self.init_sales_view()
        self.init_customers_view()

        left_upper = QScrollArea(self)
        left_upper.setWidgetResizable(True)
        left_upper.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(left_upper)

        widget_for_left_upper = QWidget()
        left_upper_layout = QVBoxLayout(widget_for_left_upper)

        # Initialize the cart view
        self.init_cart_view(left_upper_layout)

        left_upper.setWidget(widget_for_left_upper)
    def close_application(self):
        self.close()

    def switch_view(self, index):
        self.stacked_widget.setCurrentIndex(index)
    def init_cart_view(self, container_widget):
        widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        try:
            for item in ProductCard.products:
                cart_component = CartComponents(item['product_name'], item['product_price'])
                container_layout.addWidget(cart_component)
        except Exception as e:
            print(f"An error occurred while processing new data: {e}")
        container_layout.addWidget(widget)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        container_layout.setSpacing(10)

        widget.setLayout(container_layout)
        widget.setMaximumWidth(600)
    def init_products_view(self):
        widget = QWidget()
        grid_layout = QGridLayout(widget)
        conn, cursor = connect_to_db()

        # data fetch
        cursor.execute('SELECT product_name, product_price FROM products')
        products = cursor.fetchall()
        print(products)
        conn.close()

        # cards
        for i, product in enumerate(products):
            product_card = ProductCard(product[0], product[1])
            grid_layout.addWidget(product_card, i // 3, i % 3)

        self.stacked_widget.addWidget(widget)

    def init_sales_view(self):
        widget = QWidget()
        grid_layout = QGridLayout(widget)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        conn, cursor = connect_to_db()

        try:
            # fetch
            cursor.execute('SELECT sale_id FROM sales')
            sales_data = cursor.fetchall()
            print("Sales Data:", sales_data)

            for i, sale in enumerate(sales_data):
                sale_card = SaleCard(sale[0])
                grid_layout.addWidget(sale_card, i // 3, i % 3)

        except Exception as e:
            print(f"An error occurred while processing sales data: {e}")

        finally:
            conn.close()

        self.stacked_widget.addWidget(widget)

    def init_customers_view(self):
        widget = QWidget()
        grid_layout = QGridLayout(widget)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        conn, cursor = connect_to_db()

        try:
            cursor.execute('SELECT customer_id FROM customers')
            customers = cursor.fetchall()

            for customer in customers:
                customer_card = CustomerCard(customer[0])
                grid_layout.addWidget(customer_card)

        except Exception as e:
            print(f"An error occurred while processing customers data: {e}")

        finally:
            conn.close()

        self.stacked_widget.addWidget(widget)

    def change_background(self, image_path):
        self.nav_bar.setStyleSheet(f"background-image: url('{image_path}');"
                                   f"background-repeat: no-repeat;"
                                   f"background-size: cover 20px;"
                                   "margin: 0; padding: 0;")

    def show_products(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_sales(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_customers(self):
        self.stacked_widget.setCurrentIndex(2)

def open_main_app(main_app, admin=False):
    try:
        main_app.close()
        coffee_shop = CoffeeShop()
        coffee_shop.show()
    except Exception as e:
        print(f"An error occurred while opening the main app: {e}")
