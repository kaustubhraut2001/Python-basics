import time 

def timer(fn):
    def wrapper(*args , **kwargs):
        start = time.time()
        res = fn(*args , **kwargs)
        end = time.time()
        print(f"Time taken to execute {fn.__name__} is {end - start} seconds") # fn have an access to __name__ attribute which will retun the name of the function which is getting execuate
        return res
    return wrapper

@timer
def add(a,b):
    time.sleep(2)
    return a+b

add(2,4)