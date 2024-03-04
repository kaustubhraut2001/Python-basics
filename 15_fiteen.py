# abstract classmethod- > methods which has only decelaeration but no implementation we can not create object of it

from abc import ABC,abstractmethod

class computer(ABC):
	@abstractmethod
	def proces():
		pass


class laptop(computer):
	def proces(self):
		print("its running")
	# pass


# c1 = computer()
# print(c1) # it will give error because we can not create object of abstract class


# c2 = laptop()
# c2.proces()


# Iteraters
nums = [8,7,6,5,4]

it = iter(nums)

#why we use it

#print(it.__next__())
#print(it.__next__())
#print(it.__next__())

#print(next(it))

class topten:
	def __init__(self ):
		self.num = 1

	def __iter__(self):
		return self


	def __next__(self):
		if self.num <= 10:
			val = self.num
			self.num += 1
			return val

		else:
			raise StopIteration


values = topten()

for i in values:
	print(i)