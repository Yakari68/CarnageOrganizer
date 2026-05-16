import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QAction, QKeySequence


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu tournoi")
        self.resize(600, 400)

        barre_menu = self.menuBar()

        # --- MENU TOURNOI ---
        menu_tournoi = barre_menu.addMenu("&Tournoi")

        action_nouveau = QAction("Nouveau", self)
        action_nouveau.setShortcut(QKeySequence.New)  # Ctrl+N
        action_nouveau.triggered.connect(self.fonction_nouveau)
        menu_tournoi.addAction(action_nouveau)

        action_reset = QAction("Réinitialiser", self)
        action_reset.setShortcut("Ctrl+R")
        action_reset.triggered.connect(self.action_reset)  # Correction nom fonction
        menu_tournoi.addAction(action_reset)

        menu_tournoi.addSeparator()

        # --- MENU BASE DE DONNÉE ---
        menu_db = barre_menu.addMenu("&Base de donnée")

        action_choix_db = QAction("Sélection base de donnée", self)
        action_choix_db.setShortcut("Ctrl+B")
        action_choix_db.triggered.connect(self.action_choix_db)
        menu_db.addAction(action_choix_db)

        action_new_db = QAction("Nouvelle base de donnée", self)
        action_new_db.triggered.connect(self.action_new_db)
        menu_db.addAction(action_new_db)

        # --- MENU EQUIPE ---
        menu_equipe = barre_menu.addMenu("&Equipe")

        action_ajout_equipe = QAction("Ajouter une équipe", self)  # Ajout de self
        action_ajout_equipe.setShortcut("Ctrl+E")
        action_ajout_equipe.triggered.connect(self.action_ajout_equipe)
        menu_equipe.addAction(action_ajout_equipe)

        action_supp_equipe = QAction("Supprimer une équipe", self)  # Ajout de self
        action_supp_equipe.setShortcut("Ctrl+W")  # Correction orthographe setShortcut
        action_supp_equipe.triggered.connect(self.action_supp_equipe)
        menu_equipe.addAction(action_supp_equipe)

        # Zone centrale
        self.label_info = QLabel("Sélectionnez une option dans le menu", self)
        self.label_info.setMargin(20)
        self.setCentralWidget(self.label_info)

    # --- DÉFINITION DES FONCTIONS (obligatoires pour éviter les erreurs) ---

    def fonction_nouveau(self):
        self.label_info.setText("Action : Nouveau Tournoi")

    def action_reset(self):
        self.label_info.setText("Action : Réinitialisation")

    def action_choix_db(self):
        self.label_info.setText("Action : Sélection DB")

    def action_new_db(self):
        self.label_info.setText("Action : Nouvelle DB")

    def action_ajout_equipe(self):
        self.label_info.setText("Action : Ajouter Équipe")

    def action_supp_equipe(self):
        self.label_info.setText("Action : Supprimer Équipe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
