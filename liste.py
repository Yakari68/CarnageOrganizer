import pandas as pd
import os
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

class Equipe(Base):
    __tablename__ = 'equipes'
    id = Column(Integer, primary_key=True)
    nom = Column(String, unique=True)
    membres = relationship("Participant", back_populates="equipe")

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    equipe_id = Column(Integer, ForeignKey('equipes.id'))
    equipe = relationship("Equipe", back_populates="membres")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# --- PHASE 1 : CRÉATION DES ÉQUIPES SI VIDE ---
if not session.query(Equipe).first():
    print("\n--- AUCUNE ÉQUIPE TROUVÉE. CRÉONS-LES ! ---")
    try:
        nb = int(input("Combien d'équipes souhaitez-vous créer ? : "))
        for i in range(nb):
            nom_eq = input(f"Nom de l'équipe {i+1} : ")
            session.add(Equipe(nom=nom_eq))
        session.commit()
        print("✅ Équipes enregistrées !")
    except ValueError:
        print("❌ Erreur : tu dois entrer un chiffre.")

# --- PHASE 2 : MENU PRINCIPAL ---
while True:
    choix = input("\nAction (ajouter / supprimer / voir / quitter) : ").lower()
    
    if choix == 'ajouter':
        prenom = input("Prénom : ")
        nom = input("Nom : ")
        eqs = session.query(Equipe).all()
        print("\nChoisir l'équipe :")
        for e in eqs:
            print(f"{e.id}: {e.nom}")
        id_eq = input("ID de l'équipe : ")
        session.add(Participant(nom=nom, prenom=prenom, equipe_id=int(id_eq)))
        session.commit()
        print(f"✅ {prenom} ajouté.")

    elif choix == 'supprimer':
        p_list = session.query(Participant).all()
        for p in p_list:
            print(f"ID: {p.id} | {p.prenom} {p.nom}")
        id_del = input("ID à supprimer : ")
        cible = session.query(Participant).get(int(id_del))
        if cible:
            session.delete(cible)
            session.commit()
            print("🗑️ Supprimé.")

    elif choix == 'voir':
        # Petit bonus pour voir les équipes sans ouvrir Excel
        for e in session.query(Equipe).all():
            print(f"\n{e.nom} ({len(e.membres)} membres) :")
            for m in e.membres:
                print(f"  - {m.prenom} {m.nom}")

    elif choix == 'quitter':
        break

# Export Excel
query = "SELECT p.prenom, p.nom, e.nom AS equipe FROM participants p LEFT JOIN equipes e ON p.equipe_id = e.id"
pd.read_sql(query, engine).to_excel("controle_equipes.xlsx", index=False)
print("\n🚀 Fichier Excel mis à jour. À bientôt !")

print("\n--- RÉCAPITULATIF DES ÉQUIPES ---")
toutes_les_equipes = session.query(Equipe).all()

for eq in toutes_les_equipes:
    print(f"\nGroupe {eq.nom}:")
    if not eq.membres:
        print("  (Aucun membre pour le moment)")
    for membre in eq.membres:
        print(f"  - {membre.prenom} {membre.nom}")