from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
class TeamDB(Base):
    __tablename__ = 'Teams'
    name = Column(String, unique=True)
    registration_date = Column(String)
    team_id = Column(String, primary_key=True)

def load_session(db_name):
    engine=create_engine(f'sqlite:///{db_name}.corgadb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def add_team(db_name=None,name=None,registration_date=None,team_id=None):
    session=load_session(db_name)
    session.add(TeamDB(name=name,registration_date=registration_date,team_id=team_id))
    session.commit()
    session.close()

def remove_team(db_name=None,team_id=None):
    session=load_session(db_name)
    team = session.query(TeamDB).filter(TeamDB.team_id == team_id).first()
    if team is not None:
        session.delete(team)
        session.commit()
    session.close()

def get_teams(db_name=None):
    session=load_session(db_name)
    team_db = session.query(TeamDB).all()
    session.close()
    return team_db
