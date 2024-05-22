from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class CustomerCard(QWidget):
    def __init__(self, customer_id, cart_callback=None):
        super().__init__()
        self.cart_callback = cart_callback
        layout = QVBoxLayout(self)

        customer_label = QLabel(f"Customer: {customer_id}", self)

        layout.addWidget(customer_label)
