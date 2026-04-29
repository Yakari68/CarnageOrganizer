import pandas as pd
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_name = 'pays_projet.db'

print("=== CONFIGURATION CARNAGE ORGANIZER ===")
reset = input("Est-ce un nouveau tournoi ? (oui/non) : ").lower()

if reset == 'oui' and os.path.exists(db_name):
    os.remove(db_name)
    print("🗑️ Base de données réinitialisée.")

# Configuration SQL
engine = create_engine(f'sqlite:///{db_name}')
Base = declarative_base()

class Team(Base):
    __tablename__ = 'Teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    membres = relationship("Participant", back_populates="Team")

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    prename = Column(String)
    team_id = Column(Integer, ForeignKey('Teams.id'))
    Team = relationship("Team", back_populates="membres")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# --- PHASE 1 : CRÉATION DES ÉQUIPES SI VIDE ---
if not session.query(Team).first():
    print("\n--- AUCUNE ÉQUIPE TROUVÉE. CRÉONS-LES ! ---")
    try:
        nb = int(input("Combien d'équipes souhaitez-vous créer ? : "))
        for i in range(nb):
            name_eq = input(f"name de l'équipe {i+1} : ")
            session.add(Team(name=name_eq))
        session.commit()
        print("✅ Équipes enregistrées !")
    except ValueError:
        print("❌ Erreur : tu dois entrer un chiffre.")

# --- PHASE 2 : MENU PRINCIPAL ---
while True:
    choix = input("\nAction (ajouter / supprimer / voir / quitter) : ").lower()
    
    if choix == 'ajouter':
        prename = input("Préname : ")
        name = input("name : ")
        eqs = session.query(Team).all()
        print("\nChoisir l'équipe :")
        for e in eqs:
            print(f"{e.id}: {e.name}")
        id_eq = input("ID de l'équipe : ")
        session.add(Participant(name=name, prename=prename, Team_id=int(id_eq)))
        session.commit()
        print(f"✅ {prename} ajouté.")

    elif choix == 'supprimer':
        p_list = session.query(Participant).all()
        for p in p_list:
            print(f"ID: {p.id} | {p.prename} {p.name}")
        id_del = input("ID à supprimer : ")
        cible = session.query(Participant).get(int(id_del))
        if cible:
            session.delete(cible)
            session.commit()
            print("🗑️ Supprimé.")

    elif choix == 'voir':
        # Petit bonus pour voir les équipes sans ouvrir Excel
        for e in session.query(Team).all():
            print(f"\n{e.name} ({len(e.membres)} membres) :")
            for m in e.membres:
                print(f"  - {m.prename} {m.name}")

    elif choix == 'quitter':
        break

# Export Excel
query = "SELECT p.prename, p.name, e.name AS Team FROM participants p LEFT JOIN Teams e ON p.Team_id = e.id"
pd.read_sql(query, engine).to_excel("controle_Teams.xlsx", index=False)
print("\n🚀 Fichier Excel mis à jour. À bientôt !")