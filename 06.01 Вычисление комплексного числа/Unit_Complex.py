
from dec import Complex

dashes = "----------------------------------------"

def Real_number(z1, z2, z3):
    return (1 / (z1.getRe() * z2.getRe())) + (z1.getRe() ** 2 + 4 * z2.getRe()) / (z3.getRe() ** 2 - 7 * z2.getRe()) - abs(z3.getRe() + 3) * (z1.getRe() - 2)

def Complex_number(z1, z2, z3):
    if z1.getIm == 0 and z2.getIm == 0 and z3.getIm == 0:
        return Complex(Real_number(z1, z2, z3))

    z = Complex()
    zz = Complex()

    part1 = Complex()

    z.setRe(1)
    zz.Mul(z1, z2)

    part1.Sub(z, zz)

    part21 = Complex()

    z.Mul(z1, z1)
    zz.Mul(Complex(4), z2)
    part21.Add(z, zz)

    part22 = Complex()

    z.Mul(z3, z3)
    zz.Mul(Complex(7), z2)
    part22.Div(z, zz)

    part2 = Complex()
    part2.Div(part21, part22)

    part3 = Complex()

    part31 = Complex()
    part31.Add(z3, Complex(3))

    zz.Sub(z1, Complex(2))
    part3.Mul(Complex(part31.Mod()), z)

    zzz = Complex()
    z.Add(part1, part2)
    zzz.Sub(z, part3)

    return zzz
