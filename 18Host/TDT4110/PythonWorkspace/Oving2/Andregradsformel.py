import cmath
import ConsoleUtil as cu


def sgn(a):
    return 1 if a >= 0 else -1


def quad_eq(a, b, c):
    x_1 = -((b + sgn(b) * cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    x_2 = c / (a * x_1)
    return (x_1, x_2)


def run():
    formating = '.3e'
    print("Skriv inn koeffisientene til en andregradsligning: ")
    a = cu.cin_F("a = ")
    b = cu.cin_F("b = ")
    c = cu.cin_F("c = ")

    ans = quad_eq(a, b, c)

    print("Andregradsligningen " + format(a, formating) + " * x^2 + " + format(b, formating) + " * x + " + format(a, formating), end=" ")

    if ans[0].imag != 0:
        print("har to imaginære løsninger:")
        print(format(ans[0].real, formating) + " + " + format(ans[0].imag, formating) + " i")
        print(format(ans[1].real, formating) + " + " + format(ans[1].imag, formating) + " i")
    elif ans[0] == ans[1]:
        print("har en reell dobbelrot:")
        print(format(ans[0].real, formating))
    else:
        print("har to reelle løsninger:")
        print(format(ans[0].real, formating))
        print(format(ans[1].real, formating))
