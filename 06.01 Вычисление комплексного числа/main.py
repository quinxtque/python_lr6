
from Unit_Complex import dashes, Complex_number, Real_number
from dec import Complex
from dec import zs

while True:
    print("\nВыберите действие:")
    print("1 - случайные значения аргументов")
    print("2 - ввод аргументов с клавиатуры")
    print("3 - выход из программы\n")

    action = int(input())
    print()

    if action == 3:
        break

    for i in range(3):
        zs.append(Complex())
        zs[i].name = f"z{i + 1}"

    if action == 1:
        for z in zs:
            z.Init_rand()

    elif action == 2:
        for z in zs:
            z.Init_keyboard()

    for z in zs:
        z.Print()

    z = Complex_number(zs[0], zs[1], zs[2])
    d = Real_number(zs[0], zs[1], zs[2])

    print("\nРезультат:\n")

    print()

    z.Print()
    print(f"\nd = {d:g}\n")

    print(dashes)
    zs.clear()
