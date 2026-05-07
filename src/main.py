import sys
from PySide6.QtWidgets import (QApplication, QWidget,
                               QVBoxLayout, QHBoxLayout, QMainWindow)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from app.logics.teams import Team
from app.ui.match import MatchWidget
from random import shuffle

if __name__=="__main__":
#     class MainWindow(QMainWindow):
#         def __init__(self, parent=None):
#             super(MainWindow, self).__init__(parent)
#             self.setWindowTitle("Test empty teams for later matchs")
#             match=MatchWidget(parent=self)
#             self.setCentralWidget(match)
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")
#             teamlist=[Team.new("Skib"),Team.new("None"),Team.new("Hava"),Team.new("Nagila")] # ,Team.new("Verdamm")]
            teamlist=[Team.new("Skib"),Team.new("None"),Team.new("Hava"),Team.new("Nagila") ,Team.new("Verdamm"),Team.new("Koftomi"),Team.new("Arsch"),Team.new("Matcha")]
            shuffle(teamlist)
            
            
            matchs=[[MatchWidget(parent=self,top_team=teamlist[i],bottom_team=teamlist[i+1]) for i in range(0,len(teamlist),2)]]
            
            current=1
            while len(matchs[current-1])!=1:
                current+=1
                matchs_to_add=[MatchWidget(parent=self) for k in range(len(matchs[current-2])//2)]
                matchs.append(matchs_to_add)
            print(matchs)
            
            main_widget=QWidget(self)
            layout=QVBoxLayout(main_widget)

            rounds=[QWidget(main_widget) for i in range(len(bin(len(teamlist)))-3)]
            rounds_layouts=[QHBoxLayout(rounds[i]) for i in range(len(rounds))]
            for i in range(len(rounds)):
                for m in matchs[i]:
                    rounds_layouts[i].addWidget(m)
            for i in range(len(matchs)):
                for m in matchs[i]:
                    rounds_layouts[i].addWidget(m)
                    # à modifier en fonction de matchs_init une fois généralisé
                    #MATCHPRECEDENT1.winner.connect(MatchWidget(rounds[i]).top_team.get_team)
                    #MATCHPRECEDENT2.winner.connect(MatchWidget(rounds[i]).top_team.get_team)
            for i in range(len(rounds)):
                print(i)
                rounds[i].setLayout(rounds_layouts[i])

            for r in rounds:
                layout.addWidget(r)
            main_widget.setLayout(layout)
            self.setCentralWidget(main_widget)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())

