def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

if __name__ == "__main__":
    print(add(1,2,3,6,4,5))