from Time import Time
"""
class <class_header>: class header defines a class.
    def __init__ (self, <optional variables>): This is a constructor. It initializes.
        self.<variable1>=<value>
        self.<variable2>=<value>
    def <method_name>: This is a method. You can think of it as a function.
        <does_something>
"""

"""
Some of the special attributes of a Class
__doc__ = Gives you a class's doc string. If it is empty it returns "None"
__module__ = Gives you the name of the file in which the class is defined.
__name__ = Gives you the class name 

"""

time1 = Time()
time2 = Time(1)  # Here you can initialize the hour only
time1.print_time()  # Here I used the print_time method of the Time class.
time2.print_time()
print(time1.__doc__)
print(time1.__module__)
