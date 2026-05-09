import sys
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIntValidator
from uuid import uuid4
# from app.logics.teams import *

class TeamCreateWidget(QWidget):
    def __init__(self,parent=None,new=True):
        super().__init__(parent)
        # Crée les widgets contenant les infos de l'équipe
        label_name=QLabel("Name :")
        self.name=QLineEdit()
        label_date=QLabel("Registration date :")
        self.datetime_edit = QDateTimeEdit()
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.datetime_edit.setDisplayFormat("dd/MM/yyyy HH:mm")
        self.datetime_edit.setCalendarPopup(True)

        id_label=QLabel("Team ID :")
        self.id=QLabel(uuid4().hex)
        create_button = QPushButton("Create team")
        create_button.clicked.connect(self.create_team)

        team_create_layout=QVBoxLayout()
        team_create_layout.addWidget(label_name)
        team_create_layout.addWidget(self.name)
        team_create_layout.addWidget(label_date)
        team_create_layout.addWidget(self.datetime_edit)        
        team_create_layout.addWidget(id_label)
        team_create_layout.addWidget(self.id)
        team_create_layout.addWidget(create_button)
        self.setLayout(team_create_layout)

    def create_team(self):
        print(self.datetime_edit.text())
#         ajoute l'équipe à la db

if __name__ == '__main__':
    class MainWindow(QMainWindow):
        def __init__(self, parent=None,new=True):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")

            team=TeamCreateWidget(parent=self,new=new)
            self.setCentralWidget(team)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())