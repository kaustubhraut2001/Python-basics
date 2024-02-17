# Scopes and Clousers

x = 99

def f1():
    x = 88
    def f2():
        global x #x we use global keywork to access the global variable
        print(x)
    f2()


f1() # 88



#  Clousers

def f3():
    x = 88 #if this x is not availe then it will point to global x
    def f4():
        print(x)  #this will from an Clousers as it is accessing the variable from the outer function nd even if there is no x avalable in the outer function it will still work as it points to global x
    return f4

action = f3()
action() # 88


# MORE BETTER EXAMPLE OF CLOUSERS
def outer(num):
    def inner(x):
        return x**num
    return inner

square = outer(2)(4) # 4**2
print(square) #16