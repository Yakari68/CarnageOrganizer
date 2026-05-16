import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from app.ui.main_widget import mainWidget
from app.ui.menu import Menu
from app.core.state import AppState
from app.logics.teams import Team
from app.database.database import load_session, TeamDB, get_teams

# A déplacer dans UI une fois l'app finie
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
        self.setCentralWidget(self.info_label)
    
    def team_list_build(self):
        team_db = get_teams(self.state.db_name)
        print(team_db)
        for team in team_db:
            self.state.teamlist.append(
                Team.new(
                    name=team.name,
                    registration_date=team.registration_date,
                    team_id=team.team_id
                )
            )

if __name__=="__main__":
    app = QApplication(sys.argv)
    state=AppState()
    window = MainWindow(state=state)
    window.show()
    sys.exit(app.exec())
