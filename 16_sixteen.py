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
from time import sleep

class Hello(Thread):
	def run(self):
		for i in range(5):
			print("Hello")
			sleep(1)




class Hi(Thread):
	def run(self):
		for i in range(5):
			print("Hi")
			sleep(1)



t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

print("Bye") # this is executed by main thread

t1.join() # main thread will wait for t1 to complete

t2.join() # main thread will wait for t2 to complete