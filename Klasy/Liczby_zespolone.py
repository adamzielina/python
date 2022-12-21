import math

class Complex(object):

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag), (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        return Complex((self.real * other.real - self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                       (self.imag * other.real + self.real * other.imag) / (other.real ** 2 + other.imag ** 2))