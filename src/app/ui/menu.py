from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction
from app.ui.team_create import manageWidget
from app.ui.settings import settingsWidget

class Menu(QMenuBar):
    def __init__(self,parent,state):
        super().__init__(parent)
        self.parent=parent
        self.state=state
        self.w=None
        team_manage=QAction("Équipes", self)
        team_manage.triggered.connect(self.launch_team_management)
        
        tournament_launch=QAction("Lancer le tournoi!", self)
        tournament_launch.triggered.connect(self.launch_tournament)
        
        settings=QAction("Paramètres",self)
        settings.triggered.connect(self.launch_settings)
        
        self.addAction(team_manage)
        self.addAction(tournament_launch)
        self.addAction(settings)
        
    def launch_team_management(self):
        self.parent.info_label.setText("Gestion des équipes")
        self.w=manageWidget(state=self.state)
        self.w.show()
        
    def launch_tournament(self):
        x=len(self.state.teamlist)
        if x > 0 and (x & (x - 1)) == 0:
            self.parent.main.build_ui()
            self.parent.setCentralWidget(self.parent.main)
        else:
            self.parent.info_label.setText("Pas assez ou trop d'équipes! Le nombre d'équipes doit être une puissance de 2: 2, 4, 8, 16...")
        
    def launch_settings(self):
        self.parent.info_label.setText("Paramètres")
        self.w=settingsWidget(state=self.state)
        self.w.show()
        