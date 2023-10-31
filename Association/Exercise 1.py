class Elevator:
    def __init__(self,Bfloor,Tfloor):
        self.Bfloor=Bfloor
        self.Tfloor=Tfloor
        self.floor=0

    def go_to_floor(self,hfloor):
        repeat=0
        while repeat<1:
            if self.floor+hfloor<self.Tfloor:
                print(f"this is floor {self.floor+hfloor}")
            else:
                print(f"this is max floor {self.Tfloor}")
            repeat+=1
    def floor_up(self):

    # def floor_down(self):
customer=Elevator(0,20)
# customer.go_to_floor(5)
# customer.go_to_floor(10)
# customer.go_to_floor(15)
# customer.go_to_floor(20)
# customer.go_to_floor(30)