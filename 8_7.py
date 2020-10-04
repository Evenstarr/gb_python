class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def __mul__(self, other):
        return f"{self.real * other.real - self.imaginary * other.imaginary} +" \
               f" {self.real * other.imaginary + other.real * self.imaginary}i"


a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a * b)
