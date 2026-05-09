from app.database.database import TeamDB, engine_builder, load_session

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
    def new(cls,name,registration_date=None,team_id=None):
        obj = cls()  # création de l'instance
        obj.name = name
        obj.registration_date = registration_date
        obj.id = team_id
        return obj