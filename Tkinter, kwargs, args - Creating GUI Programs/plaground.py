def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(3, 5, 6, 20, 9)


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(10, add=3, multiply=5)


# get()
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Audi", model="A3", color="Blue")
print(my_car.make)
print(my_car.model)
print(my_car.color)
