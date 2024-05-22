from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout

class CartPage(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_products = []

        self.setWindowTitle("Sepet")
        self.setGeometry(1300, 0, 600, 500)


        layout = QVBoxLayout(self)

        self.cart_label = QLabel(self)
        self.cart_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.cart_label)

        buttons_layout = QVBoxLayout()

        self.reset_button = QPushButton("Reset", self)
        self.buy_button = QPushButton("Buy", self)

        buttons_layout.addWidget(self.reset_button)
        buttons_layout.addWidget(self.buy_button)

        layout.addLayout(buttons_layout)

        self.reset_button.clicked.connect(self.reset_cart)
        self.buy_button.clicked.connect(self.buy_cart)

    def add_to_cart(self, cart_item_details):
        try:
            self.list_products.append(cart_item_details)
            print(self.list_products)
            self.update_cart_label()
            self.cart_updated.emit()
        except Exception as e:
            print(f"An error occurred while adding to cart: {e}")

    def reset_cart(self):
        self.list_products.clear()
        self.update_cart_label()

    def buy_cart(self):
        total_price = sum(item['product_price'] for item in self.list_products)
        print(f"Total Price: ${total_price}")

        # Emit the signal with the current list_products
        self.cart_updated.emit(self.list_products)

        self.reset_cart()

    def update_cart_label(self):
        # Update the label with the current list_products information
        label_text = "\n".join([f"{item['product_name']} - ${item['product_price']}" for item in self.list_products])
        self.cart_label.setText(label_text)
