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
        return self.__name #why we use __name because we want to restrict the access of the variable to the outside world
    
    def get_marks(self):
        return self.__marks #__ means private variable no other can accss it only the class can access it an its function
    
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


# Polymorphism 
class car:

    total=0
    def __init__(self, name):
        self.name = name
        car.total += 1 
        #self.total = car.total #this is the class variable

    def cartype(self):
        return "Disel Car"
    

class electric_car(car):
    def __init__(self, name, battery):
        super().__init__(name)
        self.battery = battery
        car.total += 1


    def cartype(self):
        return "Electric Car"

c1 = car("BMW")
c2 = electric_car("Tesla", "100kWh")
print(c1.cartype()) #Disel Car
print(c2.cartype()) #Electric Car
print(car.total) #3


#static methods
# this is avalable to the class butnot available to the object of the class

class car:
    def __init__(self, name):
        self.name = name

    def general_description(self):
        return "This is a car"

    @staticmethod #this is a decorator to make the method static
    # def static_method(self): #we can not use self keyword here as it is a static method
    def static_method():
        return "This is a static method"

c1 = car("BMW")
print(c1.general_description()) #This is a car
print(c1.general_description())
print(car.static_method()) #This is a static method As we can not able to access the static metod with c1 we needs to use car for it to access it.


# Deecorators
# Decorators are used to modify the behavior of function or class method
class car:
    def __init__(self, name , model):
        self.name = name
        self.__model = model

    def general_description(self):
        return "This is a car"


    @property #this decorator is used to make the method as a property this willnot change the method to property but it will change the way to access the method
    def get_model(self):
        return self.__model

    @staticmethod
    def static_method():
        return "This is a static method"

    @classmethod
    def class_method(cls): #cls is used to access the class variable
        return cls

c1 = car("BMW", "X1")
print(c1.general_description()) #This is a car
print(c1.general_description())



# class inheritance and isInstance
class car:
    def __init__(self, name , model):
        self.name = name
        self.__model = model


class electric_car(car):
    def __init__(self, name, model, battery):
        super().__init__(name, model)
        self.battery = battery

    

c1 = car("BMW", "X1")
c2 = electric_car("Tesla", "Model S", "100kWh")
isinstance(c1, car) #True
isinstance(c2, car) #True


# Multiple inheritance
class battery:
    def __init__ (self, battery):
        self.battery = battery

    
class Engine:
    def __init__(self, engine):
        self.engine = engine

    
class electric_car(battery, Engine):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine
