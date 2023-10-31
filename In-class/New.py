# class Car:
#     def __init__(self,name,distance):
#         self.name=name
#         self.distance=distance
#     def __str__(self):
#         return self.name+ " " + str(self.distance)
# class Race:
#     def __init__(self,name,distance):
#         self.name=name
#         self.distance=distance
#         self.list=[]
#     def adding(self,car):
#         self.list.append(car)
#     def show_info(self):
#         for car in self.list:
#             print(car)
#
#
# Porche=Car("abc",0)
# Phu_tho=Race("phu_tho",150)
# Phu_tho.adding(Porche)
# Audi=Car("bcd",0)
# Phu_tho.adding(Audi)
# Phu_tho.show_info()
for nums in range(1,4):
    print(f"ABC-{nums}")