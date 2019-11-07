class SomeClass:
    def __init__(self):
        self.__hidden = 0

    @property
    def some_property(self):
        return self.__hidden + 42

    @some_property.setter
    def some_property(self, value):
        if 42 <= value <= 100:
            self.__hidden = value - 42
        else:
            print("Can't")

o = SomeClass()
x = o.some_property
print(o.some_property)
o.some_property = x + 10
print(o.some_property)
