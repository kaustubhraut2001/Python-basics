# Inner  Classes

class Outer:
	def __init__(self , name , laptop):
		print("Outer class object creation")
		self.name = name
		self.laptop = self.Inner()




	class Inner:
		def __init__(self):
			self.brand = "hp"
			self.config = "i5"
			self.ram = 8

		def show(self):
			print(f"Laptop brand {self.brand} and config {self.config} and ram {self.ram}")

o = Outer("Rahul" , "hp")
print(o.laptop.show())


#inheritance

class A:
	def __init__(self):
		print("A init")

	def featurea():
		print("Feature A")

class B(A):
	def __init__(self):
		print("B init")
		super().__init__()

	def featureB():
		print("Feature B")

# class Y(A,B):
# 	def featureC():
# 		print("Feature C")
# Method Resolution order is from left to right
o = B()


