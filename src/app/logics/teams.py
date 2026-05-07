from app.logics.id_creator import id_creator

class Team():
    def __init__(self):
        self.id=None
        self.name=None
        self.registration_date=None

    def build_id(self,date):
        r=id_creator(date)
        return r
    
    @classmethod
    def from_db(cls,dboptionswhateveridk):
        try:
            connexion = sdlite3.connect("./projet.db")
        except:
            print("Problème avec le fichier")
            quit()
    
    @classmethod
    def new(cls,name,registration_date=20260101212121):
        obj = cls()  # création de l'instance
        obj.name = name
        obj.registration_date = registration_date
        obj.id = obj.build_id(obj.registration_date)
        return obj
#         Add to DB