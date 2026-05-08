from sqlalchemy import *
from sqlalchemy.orm import *
# from app.logics.teams import Team

if __name__=="__main__":
    db_name="Test"
    engine = create_engine(f'sqlite:///{db_name}.corgadb')
    Base = declarative_base()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
#     ekip=Team.from_db(None)
