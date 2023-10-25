# class pet():
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def setname(self,name):
#         self.name=name
#         print("name is change")
#     def getcolor(self):
#         return self.color
#     def bark(self,times):
#         for i in range(times):
#             print("bark bark")
# dog=pet("snowy","white")
# cat=pet("chiko","grey")
# snake=pet("python","yellow")
# print(dog.name,dog.color)
# print(cat.name,cat.color
# print(snake.name,snake.color)
# dog.setname("blabla")
# print(dog.name)
# dog.getcolor("black")

# class student():
#     counter=0
#     def __init__(self,name,age,major):
#         self.name=name
#         self.age=age
#         self.major=major
#         student.counter+=1
#     def change_name(self,name):
#         self.name=name
#         print("the name has changed")
#     def changeage(self,age):
#         self.age=age
#         print("the age has changed")
#     def changemajor(self,major):
#         self.major=major
#         print("the major has changed")
#
# first_student=student("vinh",21,"IT")
# print(first_student.name,first_student.age,first_student.major)
# second_student=student("huy",20,"IT")
# print(second_student.name,second_student.age,second_student.major)
# print(student.counter)
#
# first_student.change_name("abc")
# print(first_student.name,first_student.age,first_student.major)
# class Teacher:
#     def __init__(self,name:str,major:str,age:int):
#         self.name=name
#         self.major=major
#         self.age=age
#     def changing_major(self,name:str,major:str):
#         self.name=name
#         self.major=major
#         print(f"Now Teacher {self.name} has changed to major {self.major}")
#     def discount(self,name,ID:int):
#         self.ID=123
#         if self.ID==123:
#             print(f"the teacher {self.name} has a discount for lunch")
#
# first_teacher=Teacher("Timo","IT",52)
# first_teacher.changing_major("Timo","IB")
# first_teacher.discount("Timo",123)
# class Circle:
#     pi=3.14159
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print("area:",self.pi*self.radius**2)
#     def perimeter(self):
#         print("perimeter:",2*self.pi*self.radius)
#
# c=Circle(20)
# c.area()
# c.perimeter()

# class Student:
#     def __init__(self):
#         self.name=input("please type your name: ")
#         self.ID=int(input("please type your ID: "))
#
#     def show(self):
#         print(f"here is name {self.name} and ID {self.ID}")
#
# vinh=Student()
# vinh.show()
# class Student:
#     def __init__(self,name:str,ID:int):
#         self.name=name
#         self.ID=ID
#     def show(self):
#         print("name is",self.name,"ID is",self.ID)
#
# vinh=Student("vinh",123)
# vinh.show()
# class Circle:
#     def __init__(self,radius:int):
#         self.pi=3.14159
#         self.radius=radius
#     def area(self):
#         print("area: ",self.pi*self.radius**2)
#     def perimeter(self):
#         print("peri:",2*self.pi*self.radius)
#     def showing_pi(self):
#         self.pi=3.14159
#         print(f"{self.pi}")
# c=Circle(10)
# print(c.pi)

# class Circle:
#     circle_list=[]
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#         self.circle_list.append(self)
#     def area(self):
#         return self.pi*self.radius**2
#     def circumference(self):
#         return 2*self.pi*self.radius
# c1=Circle(10)
# c2=Circle(20)
# print(c1.area())
# print(c2.circumference())
class Person:
    def __init__(self,name:str,height:int):
        self.name=name
        self.height=height
    def __str__(self):
        return self.name
class Room:
    def __init__(self):
        self.persons=[]
    def adding(self,person:Person):
        self.persons.append(person)
    def empty(self):
        return len(self.persons)==0
    def printing_info(self):
        total_height=0
        for person in self.persons:
            total_height+=person.height
        print(f"there are {len(self.persons)}"
               f"persons in the room,and their combined height is"
                f"{total_height}cm")
        for person in self.persons:
            print(f"{person.name} ({person.height}cm)")
    def tallest(self):
        tallest_person=None
        height_of_tallest=0
        for person in self.persons:
            if tallest_person is None or person.height>height_of_tallest:
                tallest_person=person
                height_of_tallest=person.height
        return tallest_person
    def remove_tallest(self):
        tallest_person=self.tallest()
        if tallest_person:
            self.persons.remove(tallest_person)
        return tallest_person
room=Room()
print("is the room empty",room.empty())
print("the tallest :",room.tallest())

room.adding(Person("Liisi",183))
room.adding(Person("Abie",187))
room.adding(Person("Vivian",162))
room.adding(Person("Albert",166))


print("is the room empty",room.empty())
print("the tallest:",room.tallest())
room.printing_info()


removed=room.remove_tallest()
print(f"Removed from room{removed.name}")
room.printing_info()
# vinh=Person("vinh",175)
# abc=Room()
# abc.adding("vinh")
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
# vinh=Student("vinh")
# print(vinh)
# class Student:
#     def __init__(self,name:str,age:int):
#         self.name=name
#         self.age=age
#     def get_age(self):
#         return print(self.age)
#
# vinh=Student("Vinh",21)
# # vinh.get_age(21)
# vinh.get_age()

class Car:
#     def __init__(self,plate_number,colour):
#         self.plate_number=plate_number
#         self.colour=colour
class Paintshop:
    def paint(self,car:Car):
        return car.colour
# car=Car("ABC-123","blue")
abc=Paintshop()
# print(abc.paint(car)
