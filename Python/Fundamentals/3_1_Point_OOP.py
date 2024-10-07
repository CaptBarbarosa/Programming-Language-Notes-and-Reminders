class Point:
    def __init__(self, x_val=0.0, y_val=0.0):
        self.__x = x_val
        self.__y = y_val

    def print_point(self):
        print(f"X: {self.__x},Y:{self.__y}")


class Employee:
    number_of_employees = 0
    max_employees = 10

    @staticmethod
    def is_crowded():
        return Employee.number_of_employees > Employee.max_employees
    
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        Employee.number_of_employees += 1
    def __str__(self): # This is known as magic method. If the user tries to print employee this will be printed.
        return "hello"


if __name__ == "__main__":
    c = Point()
    c.__x = 10  # It doesn't affect the private variable.
    c.print_point()
    emp = Employee("John", "Doe")
    print(emp) 
