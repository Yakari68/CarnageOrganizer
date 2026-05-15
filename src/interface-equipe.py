import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.title = "Créer équipe"
        self.create_button = QPushButton("Créer")
        self.cancel_button = QPushButton("Annuler")
        self.message_1 = QLabel("Nom équipe")
        self.message_2 = QLabel("Date")
        self.message_3 = QLabel("Id : ")  # Id générer aléatoirment et à récupérer

        self.layout = QVBoxLayout(self)
        self.layout.add_widget(self.message_1)
        self.layout.add_widget(self.message_2)
        self.layout.add_widget(self.message_3)
        self.layout.add_widget(self.create_button)
        self.layout.add_widget(self.cancel_button)

        # apply the button
        self.create_button.clicked.connect(self.confirm_creation)
        self.cancel_button.clicked.connect(self.confirm_cancel)
