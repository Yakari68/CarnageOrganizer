from app.logics.id_creator import id_creator

class Team():
    def build_id(self,date):
        r=id_creator(date)
        print(r)
        return r
    
    @classmethod
    def from_db(cls,dboptionswhateveridk):
        pass
#         Import data from db
    
    @classmethod
    def new(cls,name,registration_date=20260101212121):
        obj = cls()  # création de l'instance
        obj.name = name
        obj.registration_date = registration_date
        obj.id = obj.build_id(obj.registration_date)
        return obj
#         Add to DB