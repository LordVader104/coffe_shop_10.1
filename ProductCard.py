from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QScrollArea


class ProductCard(QWidget):
    addedToCart = pyqtSignal(dict)
    products = []
    def __init__(self, product_name, product_price):
        super().__init__()

        self.product_name = product_name
        self.product_price = product_price
        self.added_to_cart = False

        layout = QVBoxLayout(self)

        name_label = QLabel(product_name, self)
        price_label = QLabel(f"Price: {product_price}", self)
        add_to_cart_button = QPushButton("Add to Cart", self)
        add_to_cart_button.clicked.connect(self.add_to_cart)

        layout.addWidget(name_label)
        layout.addWidget(price_label)
        layout.addWidget(add_to_cart_button)

    def add_to_cart(self):
        try:
            if not self.added_to_cart:
                cart_item_details = {
                    'product_name': self.product_name,
                    'product_price': self.product_price,
                }
                print("Adding to cart:", cart_item_details)

                ProductCard.products.append(cart_item_details)
                self.added_to_cart = True

                # Emit the signal to notify the main window to update the cart view
                self.addedToCart.emit(cart_item_details)
                print("Current products:", ProductCard.products)
        except Exception as e:
            print(f"Error in add_to_cart: {e}")
