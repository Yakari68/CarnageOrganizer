import sys
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QIntValidator
from uuid import uuid4
from app.database.database import *
from app.logics.teams import *
from app.core.state import AppState

class TeamCreateWidget(QWidget):
    upd_req = Signal()
    
    def __init__(self,parent=None):
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

    def create_team(self,checked=False,db_name='MyTeams'):
        session=load_session(db_name)
        add_team(self.name.text(),
                 self.datetime_edit.text(),
                 self.id.text(),
                 session)
        
        session.close()
        self.emit_update_request()

    def emit_update_request(self):
        self.upd_req.emit()
        self.id.setText((uuid4().hex))



class TeamManageWidget(QWidget):
    def __init__(self,parent=None,state=None):
        super().__init__(parent)
        self.state=state
        team_list=QLabel("Liste des équipes")
        self.manage_layout=QVBoxLayout()
        self.manage_layout.addWidget(team_list)
        self.setLayout(self.manage_layout)
    
    def update_team_list(self,db_name='MyTeams'):
        self.state.teamlist=[]
        session=load_session(db_name)
        team_db = session.query(TeamDB).all()
        session.close()
        print(team_db)
        for team in team_db:
            self.state.teamlist.append(
                Team.new(
                    name=team.name,
                    registration_date=team.registration_date,
                    team_id=team.team_id
                )
            )
        print(self.state.teamlist)
        label_list=[]
        for team in self.state.teamlist:
            label_list.append(QLabel(team.name))
        for label in label_list:
            self.manage_layout.addWidget(label)
        
class manageWidget(QWidget):
    def __init__(self,parent=None,state=None):
        super().__init__(parent)
        team=TeamCreateWidget(parent=self)
        team_manage=TeamManageWidget(parent=self,state=state)
        mwlayout=QHBoxLayout()
        mwlayout.addWidget(team)
        mwlayout.addWidget(team_manage)
        self.setLayout(mwlayout)
        team.upd_req.connect(team_manage.update_team_list)

class manageWindow(QMainWindow):
    def __init__(self, parent=None, state=None):
        super().__init__(parent)
        self.state=state
        # Définition du titre de la fenêtre
        self.setWindowTitle("Création et gestion des équipes")
        mw=manageWidget(parent=self,state=state)
        self.setCentralWidget(mw)
