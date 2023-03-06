class Ball:
    # class object attribute

    pi = 3.14

    def __init__(self, radius = 10):
        self.radius = radius
        print("that's the ball")
    # methods

    def calculateArea(self):
        return 4 * self.pi * (self.radius**2)

    def calculatePerimeter(self):
        return 2 * self.pi * self.radius

    def calculateVolume(self):
        return (4/3) * self.pi * (self.radius**3)

ball1 = Ball()   # radius = 10
ball2 = Ball(15) # radius = 15

print(f"Ball1 \n Area:{ball1.calculateArea()}, Perimeter:{ball1.calculatePerimeter()}, Volume:{ball1.calculateVolume()}")
print(f"Ball2 \n Area:{ball2.calculateArea()}, Perimeter:{ball2.calculatePerimeter()}, Volume:{ball2.calculateVolume()}")






