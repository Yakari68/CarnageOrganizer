class Team():
    def __init__(self):
        self.id=None
        self.name=None
        self.registration_date=None

    @classmethod
    def new(cls,name,registration_date=None,team_id=None):
        obj = cls()  # création de l'instance
        obj.name = name
        obj.registration_date = registration_date
        obj.id = team_id
        return obj