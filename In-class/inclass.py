class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor request")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            print(f"Running Elevator {elevator_number} from floor {elevator.current_floor} to floor {destination_floor}")
            elevator.go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number} does not exist in the building")

if __name__ == "__main__":
    # Create a building with 3 elevators from floor 1 to 10
    building = Building(bottom_floor=1, top_floor=20, num_elevators=3)

    # Run the elevators in the building
    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 3)
    # building.run_elevator(3, 7)  # This elevator does not exist
    building.run_elevator(0,9)
