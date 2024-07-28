# The *args and **kwargs gives you the opportunity to have infinite arguments
# Generally, it is used so that the arguments can be sent to other functions.

def named(name, age):
    print(name, age)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")

details= {"name":"Bob", "age":25}
named(*details) # Will print name age    
named(**details) # Will print Bob  25
print_nicely(**details)





def both_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

both_args_and_kwargs(1, 3, 5, name="Bob", age=25)
"""
The 1, 3 and 5 is hold in args and name and age will be kept in kwargs.
If you want to hold in kwargs you need to specify it with name= type of details.
"""


def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza. With the following toppings:")
    for elements in toppings:
        print(elements)
    for delivery, tip in details.items():
        print(f"Has been delivered: {delivery}, Tip amount: {tip}")

order_pizza("large", "Pepperoni","Olives", delivery=True, tip=5)
