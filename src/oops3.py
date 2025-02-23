class Circle:
    # class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        return 2 * Circle.pi * self.radius


if __name__ == "__main__":
    circle = Circle(radius=100)
    print(circle.radius)
    # Takes default value 1
    circle2 = Circle()
    print(circle2.radius)

    print(circle.area())

    circle.set_radius(10)
    print(circle.area())
    print(circle.get_radius())
    print(circle.perimeter())
