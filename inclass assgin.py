# class Visitor:
#     def __int__(self,name:str,height:int)   :
#         self.name=name
#         self.height=height
#     def __str__(self):
#         return self.name
#
# class Attractions:
#     def __init__(self):
#         self.visitors=[]
#     def store(self,visitor:Visitor):
#         self.visitors.append(visitor)
#     def checking(self,visitor,height):
#
#     def printing(self):
#         for visitor in self.visitors:
#             print(visitor)
#         print(f"there are {len(self.visitors)} visitors")
#
#
class Car:
    def __init__(self,regis_number:int,color:str):
        self.regis_number=regis_number
        self.color=color
class PaintStudio:
    def paint(self,car,color):
        car.color=color

car1=Car(123,"red")
print("this car is "+car1.color)

paint_studio=PaintStudio()
paint_studio.paint(car1,"Blue")
print("this car now is in"+car1.color)