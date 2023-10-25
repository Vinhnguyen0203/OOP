
# class Car:
#     def __init__(self,make:str,model:str,year:int):
#         self.make=make
#         self.model=model
#         self.year=year
#     def showing_info(self):
#         return self.make+" "+self.model+" "+str(self.year)
#
# huyndai=Car("titan","Ace",2023)
# # print(huyndai.showing_info())
# print(Car.showing_info(huyndai))
'''class Employee:
    raise_amount=1.04
    number_of_employees=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ "." + last + "@company.com"
        Employee.number_of_employees+=1
    def fullname(self):
        return self.first+ " " +self.last
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        return self.pay
print(Employee.number_of_employees)
vinh=Employee("The Vinh","Nguyen",5000)

huy=Employee("Khai Huy","Truong",6000)
vinh.raise_amount=1.05

print(vinh.raise_amount)
print(vinh.apply_raise())
trung=Employee("Viet Trung","Doan",7000)
print(Employee.number_of_employees)
print(Employee.raise_amount)
'''
