# creating vahicle Class
class Vehicle:
    
    def __init__(self, name, max_speed, mileage, fuel):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage 
        self.fuel = fuel
        
    def get_speed(self):
        print("The maximum speed is {} km/h".format(self.max_speed))
    
    def get_mileage(self):
        print(f"It has mileage of {self.mileage} miles per litre of {self.fuel}")
        
    def get_name(self):
        print("It's name is {}".format(self.name))        
    
# this class inherits all the methods from the Vehicle class     
class Bus(Vehicle):
    pass   
   
def main():
    # bus1 = Bus("BRT", 80, 23,'deisel')
    
    # #vehicle = Vehicle()----
    
    # bus1.get_name( )
    # bus1.get_mileage()
    # bus1.get_speed()
    
    car1 = Vehicle("mercedes", 380, 3,'HIGH OCTANE')
    bus1.get_name( )
    bus1.get_mileage()
    bus1.get_speed()
    
main()     