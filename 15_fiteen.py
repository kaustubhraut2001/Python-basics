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

print(it.__next__())
print(it.__next__())
print(it.__next__())