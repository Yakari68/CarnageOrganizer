import sys
import datetime as dt
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIntValidator
# from app.logics.teams import *

# class DateWidget(QWidget):
#     def __init__(self,new,parent=None):
#         super().__init__(parent)
#         if new==True:
#             now=dt.datetime.now()
#             day=now.day
#             month=now.month
#             year=now.year
#             hours=now.hours
#             minutes=now.minutes
#         else:
#             pass
#         
#         widget_day=QLineEdit(text=day,validator=DAYVAL)
#         date_layout=QHBoxLayout()
#         date_layout.addWidget(widget_day)
#         date_layout.addWidget(widget_month)
#         date_layout.addWidget(widget_year)
#         time_layout=QHBoxLayout()
#         time_layout.addWidget(widget_hours)
#         time_layout.addWidget(widget_minutes)
#         
#         dt_layout=QVBoxLayout()
#         dt_layout.addWidget(date_widget)
#         dt_layout.addWidget(time_widget)
#         self.setLayout(dt_layout)

class TeamCreateWidget(QWidget):
    def __init__(self,parent=None,new=True):
        super().__init__(parent)
        # Crée les widgets contenant les infos de l'équipe
        self.label_name=QLabel("Name :")
        self.name=QLineEdit()
        self.label_date=QLabel("Registration date :")
#         self.creation_date=DateWidget(self)
        self.id_label=QLabel("Team ID :")
#         self.id=QLabel()
        self.create_button = QPushButton("Create team")
        self.create_button.clicked.connect(self.create_team)

        team_create_layout=QVBoxLayout()
        team_create_layout.addWidget(self.label_name)
        team_create_layout.addWidget(self.name)
        team_create_layout.addWidget(self.label_date)
#         team_create_layout.addWidget(self.creation_date)
        team_create_layout.addWidget(self.id_label)
#         team_create_layout.addWidget(self.id)
        team_create_layout.addWidget(self.create_button)
        self.setLayout(team_create_layout)

    def eventFilter(self,obj,event):
        if (event.type() == QEvent.KeyPress) and (obj is self):
            if (event.key() in (Qt.Key_Return,Qt.Key_Enter)
            and (self.top_team_widget.team_score_widget.hasFocus()
            or self.bottom_team_widget.team_score_widget.hasFocus())):
                # Ajouter la mise à jour de la DB
                self.display_results()
        return super().eventFilter(obj, event)
    
    def create_team(self):
        pass

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