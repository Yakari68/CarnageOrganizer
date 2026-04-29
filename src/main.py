import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMainWindow
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator
from app.logics.teams import *
from app.ui.match import *

if __name__=="__main__":
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

            # Définition du titre de la fenêtre
            self.setWindowTitle("Hello!")
            
            # à sortir!
            skib=Team.new("Skib")
            none=Team.new("None")
            hava=Team.new("Hava")
            match=MatchWidget(parent=self,top_team=skib,bottom_team=none)
#             match2=
            self.setCentralWidget(match)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())
