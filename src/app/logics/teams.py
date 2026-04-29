from app.logics.id_creator import id_creator

class Team():
    def __init__(self):
        self.id=None
        self.name=None
        self.registration_date=None

    def build_id(self,date):
        r=id_creator(date)
        print(r)
        return r
    
    @classmethod
    def from_db(cls,dboptionswhateveridk):
        try:
            connexion = sdlite3.connect("C:/Users/manon/Documents/ENSISA/Semestre2/Python/Projet/CarnageOrganizer/pays_projet.db")
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