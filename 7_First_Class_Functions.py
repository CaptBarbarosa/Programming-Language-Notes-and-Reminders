
def add(x, y):
    return x + y

f = add # Now the f can be used as a function. Below, you'll see that add and f prints the same thing
print(add)
print(f)

result = f(3,4)
print(result)


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result=calculate(5,6, operator=divide)
print(f"Result is: {result}")

result=calculate(5,0, operator=divide)
print(f"Result is: {result}")



