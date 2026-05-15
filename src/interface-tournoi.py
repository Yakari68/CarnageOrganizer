import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

"""à mettre è la suite du bouton tournoi dans le menu"""


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.start_button = QPushButton("Démarrer tournoi")
        self.reset_button = QPushButton("Reset tounoi")

        self.layout = QVBoxLayout(self)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.reset_button)

        # apply the button
        self.start_button.clicked.connect(self.confirm_creation)
        self.reset_button.clicked.connect(self.confirm_cancel)
