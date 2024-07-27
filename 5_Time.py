class Time:
    """
    Dynamism of python allows the executing applications to change.
    To prevent it we can have the __slots__ attribute.
    """
    #__slots__ = ["hour", "minute", "second"]

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print(f"Hour: {self.hour}, minute: {self.minute}, second: {self.second}")

    def __setattr__(self, key, value):  # The attribute names in setattr must match the attributes in init
        if key == "hour":
            if 0 <= value < 24:
                self.__dict__[key] = value
            else:
                raise ValueError("Hour can't be more than 24 or less than 0")
        elif key == "minute" or key == "second":
            if 0 <= value < 60:
                self.__dict__[key] = value
            else:
                raise ValueError("It can't be more than 60 or less than 0")

    def __getattr__(self, item):
        if item == "hour":
            return self.hour
        elif item == "minute":
            return self.minute
        elif item == "second":
            return self.second
        else:
            raise AttributeError(item)
