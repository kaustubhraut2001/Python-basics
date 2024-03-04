# Generators
# Generators are iterators, but you can only iterate over them once.
# They do not store all the values in memory, they generate the values on the fly

def topten():
	yield 1



values = topten()
print(values.__next__())




# Erros and exception handeling


#  Multi threading

from  threading import *
class Hello(Thread):
	def run(self):
		for i in range(5):
			print("Hello")




class Hi(Thread):
	def run(self):
		for i in range(5):
			print("Hi")



t1 = Hello()
t2 = Hi()

t1.start()
t2.start()