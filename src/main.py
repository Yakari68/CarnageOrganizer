import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from app.ui.main_widget import mainWidget
from app.ui.menu import Menu
from app.core.state import AppState
from app.logics.teams import Team
# A trier une fois la barre de menu ajoutée
from app.database.database import *

# Enlevé à terme, sera lancé par une barre de menu
from app.ui.team_create import manageWindow

# A déplacer dans UI une fois l'app finie
class MainWindow(QMainWindow):
    def __init__(self, parent=None,state=None):
        super(MainWindow, self).__init__(parent)
        self.state=state
        self.setWindowTitle("CarnageOrganizer")
        self.main=mainWidget(self,state)
        self.menu=Menu(self)
        self.ready_button=QPushButton("Ready ?")
        self.ready_button.clicked.connect(self.launch_tournament)
        self.setMenuBar(self.menu)
        self.setCentralWidget(self.ready_button)
        
        
    def launch_tournament(self):
        self.main.build_ui()
        self.setCentralWidget(self.main)


if __name__=="__main__":
    app = QApplication(sys.argv)
    state=AppState()
    session=load_session('MyTeams')
    team_db = session.query(TeamDB).all()
    session.close()
    print(team_db)
    for team in team_db:
        state.teamlist.append(
            Team.new(
                name=team.name,
                registration_date=team.registration_date,
                team_id=team.team_id
            )
        )
    window = MainWindow(state=state)
    window.show()
    sys.exit(app.exec())
#  
 
### TESTS
# if __name__ == '__main__':
#     # Create the Qt Application
#     app = QApplication(sys.argv)
#     state=AppState()
#     # Create and show the app
#     window = manageWindow(state=state)
#     window.show()
#     # Run the main Qt loop
#     sys.exit(app.exec())