import time 

def timer(fn):
    def wrapper(*args , **kwargs):
        start = time.time()
        res = fn(*args , **kwargs)
        end = time.time()
        print(f"Time taken to execute {fn.__name__} is {end - start} seconds") # fn have an access to __name__ attribute which will retun the name of the function which is getting execuate
        return res
    return wrapper

@timer #this is a decorator this function will always call the timer function and pass the add function to it
def add(a,b):
    time.sleep(2)
    return a+b

add(2,4)




def debug(fn):
    def wrapper(*args , **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key} = {value}" for key , value in kwargs.items())
        print(args_value , kwargs_value)
        return fn(*args , **kwargs)
    return wrapper

@debug
def greet(name , msg = "Hey, Have a good day"):
    print(f"Hello {name} {msg}")

greet("Rahul")




def cache(fn):
    cachevalue = {}
    def wrapper(*args , **kwargs):

        print("This is a cache function" , cachevalue)
        if args in cachevalue:
            return cachevalue[args]

        res = fn(*args , **kwargs)
        cachevalue[args] = res
        return res
    return wrapper


@cache
def long_running_function():
    print("This is a long running function")
    time.sleep(5)
    return 5

print(long_running_function())