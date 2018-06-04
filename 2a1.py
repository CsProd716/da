class Vehicle:
    def __init__(self,wheels):
        print("Vehicle class called")
        self.wheels = wheels
    def num_of_wheels(self):
        print("Number of wheels: ",str(self.wheels))

def Bike(Vehicle):
    def __init__(self):
        print("Bike subclass called")
        super().__init__(2)

def Car(Vehicle):
    def __init__(self):
        print("Car subclass called")
        super().__init__(4)

def pedal_bike(Bike):
    def __init__(self):
        print("Pedal Bike sub-subclass called")
        super().__init__()

def motor_bike(Bike):
    def __init__(self):
        print("Motor Bike sub-subclass called")
        super().__init__()
        
        
