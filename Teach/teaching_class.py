
class Animal:
    def __init__(self):
        self.age = 0
        self.leg = 4
        self.wing = "no"

    def shout(self):
        print("growl")


class Duck(Animal):
    def __init__(self):
        super().__init__()
        self.leg = 2
        self.wing = "yes"

    def shout(self):
        print("꽥꽥")


a = Duck()
print(a.age)
a.age = 5
print(a.age)
