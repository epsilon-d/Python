class Triangle:
    base = 0
    height = 0

    def set_length(self, a, b):
        a = self.base
        b = self.height

    def print_area(self):
        area =
        return area


class RATriangle(Triangle):
    def print_hypotenuse(self):
        c = (self.a ** 2 + self.b ** 2) ** (1/2)
        return c


'''
x = Triangle()
x.base = 5
x.height = 4
print(x.print_area())
'''

Triangle.set_length(5, 4)