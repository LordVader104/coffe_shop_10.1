from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class SaleCard(QWidget):
    def __init__(self, sale_id, cart_callback=None):
        super().__init__()
        self.cart_callback = cart_callback
        layout = QVBoxLayout(self)

        sale_label = QLabel(f"Sale ID: {sale_id}", self)

        layout.addWidget(sale_label)


