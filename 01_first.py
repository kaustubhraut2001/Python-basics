# file is also iterable just like list, string, tuple etc.
# __next__  and __iter__ are the two methods that are used to iterate over the file.
# just smme we can write next() and iter() for file also.

# FOR FILES:
# readline for file handle the exception of EOF automatically.
# but next() does not handle the exception of EOF automatically.


# when we have multiple arguments to pass to a function, we can use *args to pass all the arguments in a tuple.
def sumall(*args):
    print(args) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(*args) #1 2 3 4 5 6 7 8 9 10
    return sum(args) #55

print(sumall(1,2,3,4,5,6,7,8,9,10))


# when we have multiple arguments to pass to a function, we can use **kwargs to pass all the arguments in a dictionary.
def printall(**kwargs):
    print(kwargs) #{'a': 1, 'b': 2, 'c': 3}
    for k in kwargs:
        print(k, kwargs[k])
    return

printall(a=1, b=2, c=3)


#generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.
def mygen(limit):
    for i in range(2,limit+5 , 2):
        return i #return will return only one value and then the function will be terminated.

# we can use yeild keyword which will return the value and the function will not be terminated.
# it will remmeber the last value and will start from there only in memory and will return the next value.


# Correct way
def mygen(limit):
    for i in range(2,limit+5 , 2):
        yield i

for num in mygen(10):
    print(num)
# print(mygen(10))