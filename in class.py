#
# class Shoppinglist:
#     def __init__(self):
#         self.items=[]
#     def add_item(self,item: str):
#         if not item in self.items:
#             self.items.append(item)
#     def print_shoppinglist(self):
#         for item in sorted(self.items):
#             print(item)
#     def longest_name(self):
#         longest=""
#         length_longest=0
#
#         for item in self.items:
#             if len(item)>=length_longest:
#                 length_longest=len(item)
#                 longest=item
#         print("the item has longest name is: ",longest)
#         return longest
# food=Shoppinglist()
# food.add_item("tomato")
# food.add_item("milk")
# food.add_item("egg")
# food.add_item("beef")
# food.add_item("cheese")
# food.print_shoppinglist()
# food.longest_name()
class Person:
    def  __init__(self,name:str,height:int):
        self.name=name
        self.height=height
    def __str__(self):
        return self.name
class Room:
    def __init__(self):
        self.persons=[]
    def add(self,person: Person):
        self.persons.append(person)
    def is_empty(self):
        return (len(self.persons))==0
    def print(self):
        total_height=0
        for person in self.persons:
            total_height+=person.height
        print(f"there are {len(self.persons)}"
              f"persons in the classroom,and their combined height is: "
              f"{total_height}cm")
        for person in self.persons:
            print(f"{person.name}is {person.height} cm")
    def tallest(self):
        tallest_person=None
        height_of_tallest=0
        for person in self.persons:
            if tallest_person is None or person.height >= height_of_tallest:
                tallest_person=person
                height_of_tallest=person.height
        return tallest_person
    def remove_tallest(self):
        tallest_person=self.tallest()
        if tallest_person:
            self.persons.remove(tallest_person)
        return tallest_person
room=Room()
print("is this room empty?",room.is_empty())
print("the tallest person is : ",room.tallest())
room.add(Person("Lihini",160))
room.add(Person("Anatoli",178))
room.add(Person("Ricardo",180))
room.add(Person("Nhi",163))
room.add(Person("Mannoc",177))
room.print()
removed=room.remove_tallest()
print(f"remove..",removed)
