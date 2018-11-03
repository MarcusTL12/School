import math as m
import ConsoleUtil as cu

def sidelength(h):
    return h * 3 / m.sqrt(6)


def area(h):
    return m.sqrt(3) * sidelength(h) ** 2


def vol(h):
    return (m.sqrt(2) / 12) * sidelength(h) ** 3


def abc():
    height = cu.cin_F("Hvor høyt er tetraederet ditt? ")
    print("Tetraeder med høyde " + str(height) + " har\nvolum: " + format(vol(height), '.3f') + "\nareal: " + format(area(height), '.3f'))
