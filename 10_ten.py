class sample:
	def __init__(self , a , b):
		print(f"these values are {a} and  {b}")


a = sample(10 , 11)

print(id(a))

b = 900
c= b
print(id(b) , id(c))

b= 1000
print(id(b), id(c))

# diffrenat types f methods class methods
# instance methods
# static method
#
class Student:
	school = "asdasd"
	def __init__(self , *args):
		self.m1 = args[0]
		self.m2 = args[1]
		self.m3 = args[2]

	def avg(self):
		return (self.m1 + self.m2 + self.m3) / 3

	def get_m1(self):
		return self.m1

	def set_m1(self, value):
		self.m1 = value


s1 = Student(10, 20, 30)
s2 = Student(40, 50, 60)

print(s1.avg())
print(s2.avg())

# Accersoes andd Mutators Methods
# on fetching values we use Accessors
# and on setting values we use Mutators





