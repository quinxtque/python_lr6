
from math import sqrt
from random import uniform

class Complex:
    def __init__(self, Re=0, Im=0, name="z"):
        self.__Re = Re
        self.__Im = Im
        self.name = name

    def Add(self, z1, z2):  # метод класса для сложения комплексных чисел
        self.__Re = z1.__Re + z2.__Re
        self.__Im = z1.__Im + z2.__Im

    def Print(self):  # вывод комплексного числа
        print(f'{self.name:2} = {self.__Re:4} + {self.__Im:5}i')

    def Sub(self, z1, z2):
        self.__Re = z1.__Re - z2.__Re
        self.__Im = z1.__Im - z2.__Im

    def Mod(self):
        return sqrt(self.__Re ** 2 + self.__Im ** 2)

    def Mul(self, z1, z2):
        self.__Re = z1.__Re * z2.__Re - z1.__Im * z2.__Im
        self.__Im = z1.__Re * z2.__Im + z1.__Im * z2.__Re

    def Div(self, z1, z2):
        z2_conjugate = Complex(z2.__Re, -z2.__Im, "z2 сопряжённое")

        numerator = Complex()
        numerator.Mul(z1, z2_conjugate)

        denominator = Complex()
        denominator.Mul(z2, z2_conjugate)

        self.__Re = numerator.__Re / denominator.__Re
        self.__Im = numerator.__Im / denominator.__Re

    def Real(self):
        return self.__Re

    def Init_rand(self):
        self.__Re = uniform(-25.00, 25.00)
        self.__Im = uniform(-25.00, 25.00)

    def getRe(self):
        return self.__Re

    def getIm(self):
        return self.__Im

    def setRe(self, Re):
        self.__Re = Re

    def setIm(self, Im):
        self.__Im = Im

    def Init_keyboard(self):
        print(self.name)
        self.__Re = float(input("Re: "))
        self.__Im = float(input("Im: "))
        print()


zs = []
