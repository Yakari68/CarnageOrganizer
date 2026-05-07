import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QVBoxLayout, QHBoxLayout, QMainWindow,
                               QLineEdit)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from app.logics.teams import Team
from app.ui.match import MatchWidget
from random import shuffle

if __name__=="__main__":
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")
            teamlist=[Team.new("Skib"),Team.new("None"),Team.new("Hava"),Team.new("Nagila"),Team.new("Verdamm")]
            shuffle(teamlist)
            matchs_init=[MatchWidget(parent=self,top_team=teamlist[i],bottom_team=teamlist[i+1]) for i in range(0,len(teamlist)-1,2)]
            mainWidget=QWidget(self)
            layout=QVBoxLayout(mainWidget)
            rounds=[QWidget for i in range(len(teamlist)+1)]
            rounds_layouts=[QHBoxLayout(rounds[r]) for r in rounds]
            for r in rounds:
                for m in matchs_init:
                    rounds_layouts.addWidget(m)
            mainWidget.setLayout(layout)
            self.setCentralWidget(mainWidget)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())
