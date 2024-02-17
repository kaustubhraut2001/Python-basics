# OOPS

class Car:
    brand = None
    name = None


a = Car()
a.brand = "BMW"
a.name = "X1"
print(a.brand, a.name)



# With constructor
class Car:
    def __init__(self, brand, name):  # __init__ is a constructor
        self.brand = brand #self i just an key work to access the variable of the class just like this in js
        self.name = name

    def full_name(self):
        return self.brand + " " + self.name

my_car = Car("BMW", "X1")
print(my_car.full_name()) #BMW X1



# Inheritance
class Eletric_Car(Car):
    def __init__(self,brand , name, battery):
        super().__init__(brand, name) #super() is used to access the parent class constructor , we can access any method of the parent class using super
        self.battery = battery #this is the new variable for the child class

    def full_name(self):
        return self.brand + " " + self.name + " " + self.battery


electic_car = Eletric_Car("Tesla", "Model S", "100kWh")
print(electic_car.full_name()) #Tesla Model S 100kWh


# Encapsulation
# Encapsulation is the concept of restricting access to certain parts of the object.
