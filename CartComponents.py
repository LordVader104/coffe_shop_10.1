from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget

class CartComponents(QWidget):
    addedToCart = pyqtSignal(dict)
    def __init__(self, product_name, product_price, remove_callback=None):
        super().__init__()

        self.product_name = product_name
        self.product_price = product_price
        self.remove_callback = remove_callback
        self.added_to_cart = True

        layout = QVBoxLayout(self)

        name_label = QLabel(product_name, self)
        price_label = QLabel(f"Price: {product_price}", self)
        remove_button = QPushButton("Remove from Cart", self)
        remove_button.clicked.connect(self.remove_from_cart)

        layout.addWidget(name_label)
        layout.addWidget(price_label)
        layout.addWidget(remove_button)

    def remove_from_cart(self):
        try:
            if self.added_to_cart and self.remove_callback:
                cart_item_details = {
                    'product_name': self.product_name,
                    'product_price': self.product_price,
                }
                print("Removing from cart:", cart_item_details)
                self.remove_callback(cart_item_details)
        except Exception as e:
            print(f"Error in remove_from_cart: {e}")
