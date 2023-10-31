import random
class Car:
    def __init__(self,regis_number,max_speed):
        self.regis_number=regis_number
        self.max_speed=max_speed
        self.current_speed=0
        self.travel_distance=0

    def plusing(self,number:int):
        self.current_speed+=number
        if self.current_speed <= 0:
            self.current_speed=0
            # print(f"the current speed after speeding {number} is {self.current_speed}")
        if self.current_speed > self.max_speed:
            self.current_speed=self.max_speed

        # print(f"the current speed after {number} is {self.current_speed} sau khi vo check")
    def drive(self,hours:int):
        distance=self.travel_distance+(self.current_speed*hours)
        self.travel_distance=distance
        print("the current travelled distance is",distance)
    def info(self):
        print(self.regis_number,",",self.max_speed,",",self.current_speed,",",self.travel_distance)
    def __str__(self):
        return f"{str(self.regis_number)},{str(self.max_speed)},{str(self.current_speed)},{str(self.travel_distance)}"
    def comparing(self,car2):
        if self.travel_distance>=car2.travel_distance:
            return self
        else:
            return car2
class Race:
    def __init__(self,name,distance):
        self.carList=[]
        self.name=name
        self.distance=distance
        self.duration = 0
        self.isWin = False
    def adding(self,car):
        self.carList.append(car)
    def timepass(self):
        self.duration+=1
        print(f"at duration = {self.duration}")
        # rd=random.randint(-10,15)
        for car in self.carList:
            # self.duration+=1
            rd = random.randint(-10, 15)
            car.plusing(rd)
            # car.plusing(rd)
            car.drive(1)
            car.info()
            if car.travel_distance >= self.distance:
                print(f"winner is {car.regis_number}")
                self.isWin = True
                break
    def show_info(self):
        for car in self.carList:
            print("day la show info")
            # print("show info: ",car.regis_number)
            print(f'regis: {car.regis_number} - max_speed: {car.max_speed}')
    def create_car(self,regis_number,max_speed):
        Audi=Car(regis_number,max_speed)
        self.carList.append(Audi)
        # self.create_car_times()
        # for  in range(1,4):
        #     print(f"ABC-{nums}")
    def create_car_times(self):
        for create in range(1,11):
            random_speed = random.randint(100, 200)
            new_name="ABC-"
            result=new_name+str(create)
            # self.create_car(create,random_speed)
            self.create_car(result,random_speed)
        # for change_name in range(1,11):
    def timepasstime(self):
        # for times in range(1,11):
        #     self.timepass()
        while self.isWin == False:
            self.timepass()


phutho=Race("phutho",2000)
phutho.create_car_times()
phutho.timepass()
phutho.timepasstime()
