# Generators
# Generators are iterators, but you can only iterate over them once.
# They do not store all the values in memory, they generate the values on the fly

def topten():
	yield 1



values = topten()
print(values.__next__())