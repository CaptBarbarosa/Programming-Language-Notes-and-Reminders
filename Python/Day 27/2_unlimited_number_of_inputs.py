def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(**kwargs): #We can also use kwargs in class creation.
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print("key: ",key, " value: ",value)
    

if __name__ == "__main__":
    print(add(1,2,3,6,4,5))
    calculate(add=3, multiply=5)
    