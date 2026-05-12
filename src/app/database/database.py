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

def add_team(name,registration_date,team_id,session):
    session.add(TeamDB(name=name,registration_date=registration_date,team_id=team_id))
    session.commit()

def get_teams(db_name):
    pass


"""
# Cette partie reste à des fins de documentation

if __name__=="__main__":
    db_name="Test"
    session = load_session(db_name)
    names = ['Skib','None','Verdamm','Hava','Nagila']
    for name in names:
        add_team(TeamDB(name=name,registration_date=str(datetime.now()),team_id=uuid4().hex))
    for e in session.query(TeamDB).all():
        print(e.name)
    session.close()
"""