from PySide6.QtWidgets import QMainWindow, QLabel, QStatusBar
from app.ui.main_widget import mainWidget
from app.ui.menu import Menu
from app.database.database import load_session, TeamDB, get_teams
from app.logics.teams import Team

class MainWindow(QMainWindow):
    def __init__(self, parent=None,state=None):
        super(MainWindow, self).__init__(parent)
        self.state=state
        self.setWindowTitle("CarnageOrganizer")
        self.team_list_build()
        self.main=mainWidget(self,state)
        self.menu=Menu(self,self.state)
        self.info_label=QLabel("Bienvenue dans CarnageOrganizer!")
        self.setMenuBar(self.menu)
        self.status_bar=QStatusBar(self)
        self.status_bar.addWidget(self.info_label)
        self.setStatusBar(self.status_bar)
        self.resize(400, 300)
    
    def team_list_build(self):
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
