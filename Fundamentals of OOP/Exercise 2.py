class Car:
    def __init__(self,registrationnumber,maximumspeed,currentspeed=0,travelleddistance=0):
        self.registrationnumber=registrationnumber
        self.maximumspeed=maximumspeed
        self.currentspeed=currentspeed
        self.travelleddistance=travelleddistance
    def show_info(self):
         print(f"regis number is '{self.registrationnumber}'\n"
            f"maximum speed is {self.maximumspeed}\n"
            f"current speed is {self.currentspeed}\n"
            f"travelled distance is {self.travelleddistance}")
    def plusing(self,number:int):
        # print(f"the current speed after {number} is {self.currentspeed}")
        self.currentspeed+=number
        if self.currentspeed <= 0:
            self.currentspeed=0
            print(f"the current speed after speeding {number} is {self.currentspeed}")
        if self.currentspeed > self.maximumspeed:
            self.currentspeed=self.maximumspeed
            print(f"the current speed after {number} is {self.currentspeed} sau khi vo check")
    def brake(self):
        result=self.currentspeed-200
        if result<0:
            result=0
        print(f"the emergy brake is {result}")


Audi=Car("ABC-123",142)
Audi.plusing(30)
Audi.plusing(70)
Audi.plusing(50)
Audi.plusing(-50)
Audi.show_info()
Audi.plusing(-50)
Audi.show_info()
Audi.plusing(-50)
Audi.show_info()
Audi.brake()








# Audi.brake()
# Porche=Car("BCD-456",200,0,0)
# Porche.show_info()
# Porche.plusing(30)
# Porche.plusing(70)
# Porche.plusing(50)
# Porche.brake()
