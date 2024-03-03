class Employee:
    def __init__(self, first, last):
        self.f_name = first
        self.l_name = last

    def __str__(self):
        return "%s %s" % (self.f_name, self.l_name)


class HourlyWorker(Employee):
    def __init__(self, first, last, init_hours=1, init_wage=2):
        Employee.__init__(self, first, last)
        self.hours = init_hours
        self.wage = init_wage

    def __str__(self):
        return "%s is an hourly worker with pay of $%.2f" % (Employee.__str__(self), self.hours*self.wage)


if __name__ == "__main__":
    slave1 = HourlyWorker("John", "Doe")
    print(slave1)
