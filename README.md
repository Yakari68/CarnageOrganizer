# CarnageOrganizer

Une application de gestion de tournois basée sur PySide6 et SQLAlchemy.

**Note Importante**

CarnageOrganizer gère les nombres d'équipes en puissances de 2 et ne renvoie que l'équipe gagnante. Pensez à bien fermer les pop-ups une fois le paramétrage fini.

# Mode d'emploi
1. Lancer main.py
2. Dans *"Paramètres"* : donner le nom de votre base de données. Vous pouvez utiliser la base de données par défaut, qui contient 4 équipes prédéfinies. Pensez à valider avant de fermer la pop-up.
3. Dans *"Équipes"* : vous pouvez voir quelles équipes existent, les supprimer, en ajouter de nouvelles. Attention, il n'y a pas de confirmation, toute modification est **DÉFINITIVE !!!**
4. Lancez le tournoi ! Donnez les scores, validez, la dernière équipe gagnante gagne le tournoi.