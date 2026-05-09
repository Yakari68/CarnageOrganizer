from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
# from app.logics.teams import Team

Base = declarative_base()
class TeamDB(Base):
    __tablename__ = 'Teams'
    name = Column(String, unique=True)
    registration_date = Column(String)
    team_id = Column(String, primary_key=True)

def engine_builder(db_name):
    return create_engine(f'sqlite:///{db_name}.corgadb')

def load_session(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__=="__main__":
# à enlever à terme!
    from datetime import datetime
    from uuid import uuid4
    class Team():
        def __init__(self):
            self.id=None
            self.name=None
            self.registration_date=None

        @classmethod
        def from_db(cls,db_name):
            engine=engine_builder(db_name)
            session = load_session(engine)
            team_db = session.query(TeamDB).first()
            try:
                return cls.new(
                    name=team_db.name,
                    registration_date=team_db.registration_date,
                    team_id=team_db.team_id
                )
            except:
                print("échec de la mission")

        @classmethod
        def new(cls,name,registration_date,team_id):
            obj = cls()  # création de l'instance
            obj.name = name
            obj.registration_date = registration_date
            obj.id = team_id
            return obj
    #         Add to DB

    db_name="Test"
    engine=engine_builder(db_name)
    session = load_session(engine)
    names = ['Skib','None','Verdamm','Hava','Nagila']
    for name in names:
        session.add(TeamDB(name=name,registration_date=str(datetime.now()),team_id=uuid4().hex))
    session.commit()
    for e in session.query(TeamDB).all():
        print(e.name)
    session.close()
    skib=Team.from_db(f"./{db_name}")
    print(skib.name)