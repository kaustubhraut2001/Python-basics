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
class student:
    def __init__(self ,name , marks):
        self.__name = name
        self.__marks = marks
    
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def set_name(self, name):
        self.__name = name
    
    def set_marks(self, marks):
        self.__marks = marks


s1= student("Rahul", 90)
print(s1.get_name()) #Rahul
print(s1.get_marks()) #90
s1.set_name("Rohan")
s1.set_marks(100)
print(s1.get_name()) #Rohan
print(s1.get_marks()) #100