import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout, QHBoxLayout, QMainWindow,
                               QLineEdit)
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
        self.team=team
#         Par défaut, affiche un texte d'attente.
#         Remplit avec le nom de l'équipe si le match
#         est un match du round 0 (première ligne de matchs)
        self.team_label=QLabel("En attente du match précédent")
        if not team==None:
            self.update_team_widget()
        self.team_score_widget=QLineEdit(text="0",validator=INT_ONLY)
            
        # Crée un layout horizontal et ajoute les widgets, puis les affiche
        self.layout=QHBoxLayout(self)
        self.layout.addWidget(self.team_label)
        self.layout.addWidget(self.team_score_widget)
        self.setLayout(self.layout)

    def score(self):
        return self.team_score_widget.text()
    
    def update_team_widget(self):
        self.team_label.setText(self.team.name)
        
# Widget général des deux équipes concurrentes
class MatchWidget(QWidget):
    winner = Signal(Team)
    
    def __init__(self,parent=None,top_team=None,bottom_team=None):
        super().__init__(parent)
        # Crée les widgets des 2 équipes et le widget général
        team_widget=QWidget(self)
        self.top_team_widget=MatchTeamWidget(team_widget,top_team)
        self.bottom_team_widget=MatchTeamWidget(team_widget,bottom_team)
        # Crée le layout vertical pour les équipes
        team_layout=QVBoxLayout()
        team_layout.addWidget(self.top_team_widget)
        team_layout.addWidget(self.bottom_team_widget)
        team_widget.setLayout(team_layout)
        
        # Crée le widget des résultats
        self.results=QLabel("En attente des scores")
        self.send_results_btn=QPushButton("Envoyer les résultats")
        self.send_results_btn.clicked.connect(self.send_results)
        results_widget=QWidget()
        results_layout=QVBoxLayout()
        results_layout.addWidget(self.results)
        results_layout.addWidget(self.send_results_btn)
        results_widget.setLayout(results_layout)
        # Crée le layout horizontal pour le match
        layout=QHBoxLayout(self)
        layout.addWidget(team_widget)
        layout.addWidget(results_widget)
        self.setLayout(layout)
        self.installEventFilter(self)
        self.update_state()
        
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
        if not self.top_team_widget.team==None and not self.bottom_team_widget.team==None:
            if self.top_team_widget.score() == self.bottom_team_widget.score():
                text="Égalité"
            elif self.top_team_widget.score() > self.bottom_team_widget.score():
                text=f"L'équipe {self.top_team_widget.team.name} gagne"
            elif self.top_team_widget.score() < self.bottom_team_widget.score():
                    text=f"L'équipe {self.bottom_team_widget.team.name} gagne"
            self.results.setText(text)
    
    def send_results(self):
        if not (self.top_team_widget.team and self.bottom_team_widget.team)==None:
            if (self.top_team_widget.score() == self.bottom_team_widget.score()):
                pass
            else:
                if(self.top_team_widget.score() > self.bottom_team_widget.score()):
                    self.winner.emit(self.top_team_widget.team)
                    print(f"{self.top_team_widget.team.name} passe au prochain match")
                if(self.bottom_team_widget.score() > self.top_team_widget.score()):
                    self.winner.emit(self.bottom_team_widget.team)
                    print(f"{self.bottom_team_widget.team.name} passe au prochain match")
    
    def top_team(self):
        return self.top_team_widget.team
    
    def bottom_team(self):
        return self.bottom_team_widget.team
    
    def set_top_team(self,team):
        self.top_team_widget.team=team
        self.top_team_widget.update_team_widget()
        
    def set_bottom_team(self,team):
        self.bottom_team_widget.team=team
        self.bottom_team_widget.update_team_widget()

    def is_ready(self):
        return not self.top_team==None and not self.bottom_team==None

    def update_state(self):
        ready = self.is_ready()
        self.send_results_btn.setEnabled(ready)
        if not ready:
            self.results_label.setText("En attente des équipes")

if __name__ == '__main__':
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")
            
            # à sortir!
            skib=Team("Skib")
            none=Team("None")
            match=MatchWidget(parent=self)
#            match=MatchWidget(parent=self,top_team=skib,bottom_team=none)
            self.setCentralWidget(match)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())