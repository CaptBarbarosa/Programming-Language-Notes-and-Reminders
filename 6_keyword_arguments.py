def named(name, age):
    print(name, age)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")



if __name__ == '__main__':
    details= {"name":"Bob", "age":25}
    #named(*details) # Will print name age
    #named(**details) # Will print Bob  25
    print_nicely(**details)