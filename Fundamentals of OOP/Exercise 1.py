class Car:
    def __init__(self,registrationnumber,maximumspeed,currentspeed=0,travelleddistance=0):
        self.registrationnumber=registrationnumber
        self.maximumspeed=maximumspeed
        self.currentspeed=currentspeed
        self.travelleddistance=travelleddistance
    def show_info(self):
        return print(f"{self.registrationnumber},{self.maximumspeed},{self.currentspeed},{self.travelleddistance}")

Audi=Car("ABC-123",142)
Audi.show_info()
