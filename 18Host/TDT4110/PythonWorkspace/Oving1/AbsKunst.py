from turtle import *
import time
 
def a():
    # setter opp tegnevinduet
    setup(330, 330, 0, 0)
    screensize(315, 315)
    goto(-60, 150)
    
    # velger farger
    bgcolor(input("Background: "))
    color(input("Square: "))
    
    # tegner den indre firkanten
    begin_fill()
    right(10) # tilter den 10 grader nedover
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    end_fill()
    setheading(0)

def toRGB(num_val: int):
    return ((num_val // (0x100 ** 2)) % 0x100, (num_val // 0x100) % 0x100, num_val % 0x100)

def b():
    # setter opp tegnevinduet
    setup(330, 330, 0, 0)
    screensize(315, 315)
    goto(-60, 150)
    
    # velger farger
    bck_col = toRGB(int(input("Background: "), 0))
    print(bck_col)
    frg_col = toRGB(int(input("Square: "), 0))
    print(frg_col)

    colormode(255)

    bgcolor(bck_col[0], bck_col[1], bck_col[2])
    color(frg_col[0], frg_col[1], frg_col[2])
    
    # tegner den indre firkanten
    begin_fill()
    right(10) # tilter den 10 grader nedover
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    end_fill()
    time.sleep(5)
    bye()
