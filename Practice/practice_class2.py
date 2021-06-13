class Triangle:
    base = 0
    height = 0

    def set_length(self, a, b):
        self.base = a
        self.height = b

    def print_area(self):
        area = self.base * self.height * (1/2)
        return area


class RATriangle(Triangle):
    def print_hypotenuse(self):
        hypotenuse = (self.base ** 2 + self.height ** 2) ** (1/2)
        return hypotenuse


x = Triangle()
x.set_length(5, 4)
print(x.print_area())

y = RATriangle()
y.set_length(3, 4)
print(y.print_hypotenuse())
