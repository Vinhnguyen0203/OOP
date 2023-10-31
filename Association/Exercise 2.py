class Elevator:
    def __init__(self,Bfloor,Tfloor):
        self.Bfloor=Bfloor
        self.Tfloor=Tfloor
        self.floor=0

    def go_to_floor(self,hfloor):
        repeat=0
        while repeat<1:
            # self.floor+=hfloor
            if 0<hfloor<=self.Tfloor:
                print(f"this is floor {hfloor}")
            elif hfloor>self.Tfloor:
                print(f"you cannot go to floor {hfloor} over {self.Tfloor}")
            elif hfloor<0:
                print(f"you cannot go to floor {hfloor} below basement")
            repeat+=1
            # self.floor+=hfloor

    def floor_up(self,up=1):
        self.floor+=up
        floor_up=self.floor
        if floor_up < self.Tfloor:
            print(f"you have been gone up {floor_up} ")
        else:
            print(f"you cannot go up because this is floor {self.Tfloor} ")
    def floor_down(self,down=1):
        self.floor-=down
        floor_down=self.floor
        if floor_down>0:
            print(f"you have been down {self.floor}")
        else:
            print("you cannot go down because this is basement")
class Building:
    def __init__(self,bFloor,tFloor,nElevator):
        self.bFloor=bFloor
        self.tFloor=tFloor
        self.nElevator=nElevator
    def run_elevator(self,elevator,distination):
        a=

Oodi=Building(1,10,3)
Oodi.run_elevator(3,2)