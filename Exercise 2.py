class Student:
    def __init__(self,name):
        self.name=name
        self.subject=[]

    def choosing(self,subject:str):
        return self.subject.append(subject)

trung=Student("Trung")
trung.choosing("Math")
trung.choosing("Physics")
Amir=Student("Amir")
Amir=Student("Amir")
Amir.choosing("Physics")
Timo=Student("Timo")
Timo.choosing("Math")
Timo.choosing("History")

