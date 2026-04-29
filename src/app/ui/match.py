import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout, QHBoxLayout, QMainWindow,
                               QLineEdit, QPushButton)
from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QIntValidator
from app.logics.teams import *


# à mettre dans les paramètres du tournoi: force à ne mettre
# que des entiers pour le score
INT_ONLY = QIntValidator() 

# Widget pour une équipe
class MatchTeamWidget(QWidget):
    def __init__(self,parent=None,team=None):
        super().__init__(parent)
        # Crée les widgets
        self.team=team
        self.team_label=QLabel(self.team.name)
        self.team_score_widget=QLineEdit(text="0",validator=INT_ONLY)

        # Crée un layout horizontal et ajoute les widgets, puis les affiche
        self.layout=QHBoxLayout(self)
        self.layout.addWidget(self.team_label)
        self.layout.addWidget(self.team_score_widget)
        self.setLayout(self.layout)

    def score(self):
        return self.team_score_widget.text()

# widget général des deux équipes concurrentes
# /!\ à ajouter: signaux d'entrée (équipes) et sortie (équipe gagnante)
class MatchWidget(QWidget):
    winner = Signal(Team)
    
    def __init__(self,top_team=None,bottom_team=None,parent=None):
        super().__init__(parent)
        self.top_team=top_team
        self.bottom_team=bottom_team
        # Crée les widgets des 2 équipes et le widget général
        self.top_team_widget=MatchTeamWidget(self,top_team)
        self.bottom_team_widget=MatchTeamWidget(self,bottom_team)
        team_widget=QWidget()
        # Crée le layout vertical pour les équipes
        team_layout=QVBoxLayout()
        team_layout.addWidget(self.top_team_widget)
        team_layout.addWidget(self.bottom_team_widget)
        team_widget.setLayout(team_layout)
        
        # Crée le widget des résultats
        self.results=QLabel("En attente des scores")
        send_results_btn=QPushButton("Envoyer les résultats")
        results_widget=QWidget()
        results_layout=QVBoxLayout()
        results_layout.addWidget(self.results)
        results_layout.addWidget(send_results_btn)
        results_widget.setLayout(results_layout)
        # Crée le layout horizontal pour le match
        layout=QHBoxLayout()
        layout.addWidget(team_widget)
        layout.addWidget(results_widget)
        self.setLayout(layout)
        self.installEventFilter(self)
        
        # Ajoute l'interaction avec le bouton: envoie l'équipe victorieuse au prochain match
        send_results_btn.clicked.connect(self.send_results)
        
    def eventFilter(self,obj,event):
        if (event.type() == QEvent.KeyPress) and (obj is self):
            if (event.key() in (Qt.Key_Return,Qt.Key_Enter)
            and (self.top_team_widget.team_score_widget.hasFocus()
            or self.bottom_team_widget.team_score_widget.hasFocus())):
                # Ajouter la mise à jour de la DB
                self.display_results()
        return super().eventFilter(obj, event)
    
    def display_results(self):
        text="En attente des scores"
        if self.top_team_widget.score() == self.bottom_team_widget.score():
            pass
        elif self.top_team_widget.score() > self.bottom_team_widget.score():
            text=f"L'équipe {self.top_team_widget.team.name} gagne"
        elif self.top_team_widget.score() < self.bottom_team_widget.score():
                text=f"L'équipe {self.bottom_team_widget.team.name} gagne"
        self.results.setText(text)
    
    def send_results(self):
        if (self.top_team_widget.score() == self.bottom_team_widget.score()):
            pass
        else:
            if(self.top_team_widget.score() > self.bottom_team_widget.score()):
                self.winner.emit(self.top_team)
                print(f"{self.top_team.name} passe au prochain match")
            if(self.bottom_team_widget.score() > self.top_team_widget.score()):
                self.winner.emit(self.bottom_team)
                print(f"{self.bottom_team.name} passe au prochain match")


if __name__ == '__main__':
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")
            
            # à sortir!
            skib=Team("Skib")
            none=Team("None")
            match=MatchWidget(parent=self,top_team=skib,bottom_team=none)
            self.setCentralWidget(match)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())