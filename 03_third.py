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






