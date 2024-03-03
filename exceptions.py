def func1(var):
    try:
        var = int(var)
        return 10/var
    except ZeroDivisionError:  # You can specify a certain error and give an error message for that manually.
        print('You can\'t enter zero ')
    except Exception as e:  # Or you can print the default exception
        print(e)


if __name__ == '_main_':
    val = input("Enter something: ")
    a = func1(val)
