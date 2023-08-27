class Car:
    color = 'Blue' #input("enter the color ")
    max_speed = 0 #int(input("enter the maximum speed "))
    acceleration = 0 #int(input("enter the acceleration "))
    tyre_friction = 0 #int(input("enter the tyre friction "))
    current_speed = 0 #int(input("enter current speed "))

    def __init__(self):
        self.is_engine_started = input("is engine started-enter yes or no ")
        print("engine should be off by default")

    def start_engine(self):
        if self.is_engine_started == 'yes':
            print("engine is started ")
        else:
            print("engine is not yet started ")

    def stop_engine(self):
        if self.is_engine_started == 'no':
            print("engine is not yet started ")
        else:
            print("engine is started ")

    def accelerate(self):
        pass

    def apply_brakes(self):
        pass

    def sound_horn(self):
        if self.is_engine_started == 'yes':
            print("Honk Honk ")
        else:
            print("Car is not yet started ")


class Truck(Car):
    max_cargo_weight = int(input("enter maximum cargo capacity"))

    def __init__(self, load):
        super().__init__()
        self.load = load
        print("load on the truck is ", load)

    def load_cargo(self):
        if self.is_engine_started == 'no':
            cargo_weight = int(input("enter cargo weight to be loaded "))
            new_cargo_weight = self.load + cargo_weight
            if new_cargo_weight <= self.max_cargo_weight:
                self.load = new_cargo_weight
                print("Truck can be loaded and current load of the truck is {}".format(new_cargo_weight))
            else:
                print("Truck cannot be loaded as cargo weight exceeds limit")
        else:
            print("Truck can not be loaded during motion")

    def unload_cargo(self):
        if self.is_engine_started == 'no':
            cargo_weight = int(input("enter cargo weight to be unloaded "))
            new_cargo_weight = self.load - cargo_weight
            if 0 <= new_cargo_weight <= self.load:
                self.load = new_cargo_weight
                print("Truck can be unloaded and current load of the truck is {}".format(new_cargo_weight))
            else:
                print("Truck cannot be unloaded as provided cargo weight exceeds limit")
        else:
            print("Truck can not be unloaded during motion")

    def sound_horn(self):
        if self.is_engine_started == 'yes':
            print("Honkk Honkk ")
        else:
            print("Truck is not started yet ")


obj1 = Car()
obj1.sound_horn()
obj2 = Truck(80)
obj2.load_cargo()
obj2.unload_cargo()
obj2.sound_horn()


