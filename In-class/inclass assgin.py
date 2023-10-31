class People:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "name is" + " "+self.name
    def sing(self):
        print(self.name+"hat")

    def show_info_person(self) :
        print(f"ten: {self.name} ")

class Room:
    def __init__(self,name):
        self.name=name
        self.peopleList=[]
    def adding(self,person):
        self.peopleList.append(person)
    def show_info(self):
        for people in self.peopleList:
            print(people)
    def do_action(self):

        # person.show_info()
        for person in self.peopleList:
            person.show_info_person()
            for sing_action in range(10):
                person.sing()





vinh=People("vinh")
mua=People("truynh")
huy=People("huynh")

first_room=Room("A33")
first_room.adding(vinh)
first_room.adding(mua)
first_room.adding(huy)
# first_room.show_info()
# first_room.do_action()
# vinh.show_info_person()
# first_room.peopleList[0].show_info_person()
# for person in first_room.peopleList:
#     person.show_info()
# for person in first_room.peopleList:
    # person.show_info_person()
first_room.do_action()
