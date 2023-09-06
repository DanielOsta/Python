def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)


calculate(5, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.make = kw.get("model")
        self.make = kw.get("color")
        self.make = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
your_car = Car(make="Nissan")
