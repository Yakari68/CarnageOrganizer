import sys
from PySide6.QtWidgets import *
from teams import *

class MatchTeamWidget(QWidget):
    def __init__(self,parent=None,team=None):
        super().__init__(parent)
        # Crée les widgets
        self.team_name=team.name
        self.team_label=QLabel(self.team_name)
        self.team_score=QLineEdit("0") # Score = 0 au début
        # Crée un layout horizontal et ajoute les widgets, puis les affiche
        self.layout=QHBoxLayout(self)
        self.layout.addWidget(self.team_label)
        self.layout.addWidget(self.team_score)
        self.setLayout(self.layout)


class MatchWidget(QWidget):
    def __init__(self,top_team=None,bottom_team=None,parent=None):
        super().__init__(parent)
        # Crée les widgets des 2 équipes
        top_team_widget=MatchTeamWidget(self,top_team)
        bottom_team_widget=MatchTeamWidget(self,bottom_team)
        # Crée le layout vertical pour un match
        self.layout=QVBoxLayout()
        self.layout.addWidget(top_team_widget)
        self.layout.addWidget(bottom_team_widget)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Définition du titre de la fenêtre
        self.setWindowTitle("Hello!")
        skib=Team("Skib")
        none=Team("None")
        match=MatchWidget(parent=self,top_team=skib,bottom_team=none)
        self.setCentralWidget(match)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())