from id_creator import id_creator

class Team():
    def __init__(self,name,registration_date=20260101212121):
        self.name=name
        self.registration_date=registration_date
#         self.id=self.build_id(self.registration_date)
#     def build_id(self,date):
#         r=id_creator(date)
#         print(r)
#         return r
