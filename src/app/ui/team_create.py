from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit,
                               QVBoxLayout, QHBoxLayout, QPushButton,
                               QDateTimeEdit)
from PySide6.QtCore import Qt, Signal, QDateTime
from PySide6.QtGui import QIntValidator
from uuid import uuid4
from app.database.database import add_team, get_teams, remove_team
from app.logics.teams import Team

class TeamCreateWidget(QWidget):
    upd_req = Signal()
    
    def __init__(self,parent=None,state=None):
        super().__init__(parent)
        self.state=state
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
        add_team(self.state.db_name,
            self.name.text(),
            self.datetime_edit.text(),
            self.id.text()
        )
        self.emit_update_request()

    def emit_update_request(self):
        self.upd_req.emit()
        self.id.setText((uuid4().hex))



class TeamManageWidget(QWidget):
    def __init__(self,parent=None,state=None):
        super().__init__(parent)
        self.state=state
        team_list=QLabel("Liste des équipes")
        list_widget=QWidget(self)
        self.list_layout=QVBoxLayout(list_widget)
        list_widget.setLayout(self.list_layout)
        self.manage_layout=QVBoxLayout(self)
        self.manage_layout.addWidget(team_list)
        self.manage_layout.addWidget(list_widget)
        self.setLayout(self.manage_layout)
        self.update_team_list()
    
    def update_team_list(self):
        self.state.teamlist.clear()
        team_db=get_teams(self.state.db_name)
        for team in team_db:
            self.state.teamlist.append(
                Team.new(
                    name=team.name,
                    registration_date=team.registration_date,
                    team_id=team.team_id
                )
            )
        teams_widget_list=[]
        while self.list_layout.count():
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                self.list_layout.removeWidget(widget)
                widget.deleteLater()
    
        for team in self.state.teamlist:
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            name=QLabel(team.name)
            delete_button = QPushButton("Suppr.")
            delete_button.clicked.connect(
                lambda checked=False, team_id=team.team_id: self.on_delete_team(team_id)
            )
            row_layout.addWidget(name)
            row_layout.addWidget(delete_button)
            row_widget.setLayout(row_layout)
            teams_widget_list.append(row_widget)
        for w in teams_widget_list:
            self.list_layout.addWidget(w)
            
    def on_delete_team(self,team_id):
        remove_team(self.state.db_name,team_id)
        self.update_team_list()
        
class manageWidget(QWidget):
    def __init__(self,state=None):
        super().__init__(None)
        self.state=state
        self.setWindowFlag(Qt.Window)
        team=TeamCreateWidget(parent=self,state=self.state)
        self.setWindowTitle("Gestion d'équipes")
        team_manage=TeamManageWidget(parent=self,state=state)
        mwlayout=QHBoxLayout()
        mwlayout.addWidget(team)
        mwlayout.addWidget(team_manage)
        self.setLayout(mwlayout)
        team.upd_req.connect(team_manage.update_team_list)

