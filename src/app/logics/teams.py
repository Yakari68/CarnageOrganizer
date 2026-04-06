from id_creator import id_creator

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
        self.name=name
        self.registration_date=registration_date
        self.id=self.build_id(self.registration_date)
#         Add to DB