class TrainCar:
    def __init__(self, car_number, passengers):
        self.car_number = car_number
        self.passengers = passengers
        self.next_car = None

class TrainSystem:
    def __init__(self):
        self.head = None

    def add_train_car(self, car_number, passengers):
        new_car = TrainCar(car_number, passengers)
        if not self.head:
            self.head = new_car
        else:
            current_car = self.head
            while current_car.next_car:
                current_car = current_car.next_car
            current_car.next_car = new_car

    def display_train(self):
        current_car = self.head
        linked_list_representation = []
        while current_car:
            linked_list_representation.append(f"Car {current_car.car_number} -> ")
            current_car = current_car.next_car
        linked_list_representation.append("None")
        print("".join(linked_list_representation))

# Create a train system
train_system = TrainSystem()

# Add train cars
train_system.add_train_car(1, 50)
train_system.add_train_car(2, 40)
train_system.add_train_car(3, 30)

# Display the train system as a linked list
train_system.display_train()