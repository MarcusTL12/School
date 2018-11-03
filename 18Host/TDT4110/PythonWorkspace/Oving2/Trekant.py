import time
from turtle import *
import random as rnd
# importerer funksjoner fra turtle

def a():
    print("Hei, jeg kan tegne en trekant")
    
    ans = input("Ønsker du spissen på trekanten opp eller ned (O / N)? ")
    
    updown = -1

    if ans.lower() == "o":
        updown = 1

    pensize(7)          # sett pennen 7 piksler tykk
    pencolor("pink")    # sett pennefargen til rosa
    bgcolor("grey")     # sett bakgrunnsfargen grå
    fillcolor("purple") # sett fyllfargen lilla
    # Tegner en fylt trekant
    begin_fill()
    forward(200)        # gå 100 piksler framover
    left(120 * updown)           # drei 120 grader venstre
    forward(200)  
    left(120 * updown)
    forward(200)
    end_fill()
    
    # Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
    time.sleep(10)

ntnucolors = (
        ("beige",   "Bg",   "#f1d282"),
        ("turkis",  "T",    "#5cbec9"),
        ("gul",     "G",    "#d5d10e"),
        ("grå",     "Gr",   "#dfd8c5"),
        ("blå",     "B",    "#79a2ce"),
        ("rosa",    "R",    "#ad208e"),
        ("lys-blå", "LB",   "#dde7ee"),
        ("brun",    "Br",   "#90492d"),
        ("lilla",   "L",    "#552988"),
        ("oransje", "O",    "#f58025")
    )

def prompt_color(message, choices):
    foundchoice = False
    index = 0
    while not foundchoice:
        print(message, end="")
        for i in choices:
            print(", NTNU-" + ntnucolors[i][0] + " (" + ntnucolors[i][1] + ")", end="")
        
        choice = input(": ")
        
        for i in choices:
            if choice == ntnucolors[i][1]:
                foundchoice = True
                index = i
        if not foundchoice:
            print(choice + " var ikke et av valgene; prøv igjen:")
    return index

def b():
    print("Hei, jeg kan tegne en trekant")

    penchoices = []
    backchoices = []
    fillchoices = []

    for i in range(3):
        j = rnd.randint(0, len(ntnucolors) - 1)
        while j in penchoices:
            j = rnd.randint(0, len(ntnucolors) - 1)
        penchoices.append(j)

        j = rnd.randint(0, len(ntnucolors) - 1)
        while j in backchoices:
            j = rnd.randint(0, len(ntnucolors) - 1)
        backchoices.append(j)
        
        j = rnd.randint(0, len(ntnucolors) - 1)
        while j in fillchoices:
            j = rnd.randint(0, len(ntnucolors) - 1)
        fillchoices.append(j)

    penchoice = prompt_color("Velg pennfarge", penchoices)
    backchoice = prompt_color("Velg bakgrunnsfarge", backchoices)
    fillchoice = prompt_color("Velg fyllfarge", fillchoices)

    pensize(7)          # sett pennen 7 piksler tykk
    pencolor(ntnucolors[penchoice][2])    # sett pennefargen til rosa
    bgcolor(ntnucolors[backchoice][2])     # sett bakgrunnsfargen grå
    fillcolor(ntnucolors[fillchoice][2]) # sett fyllfargen lilla
    # Tegner en fylt trekant
    begin_fill()
    forward(200)        # gå 100 piksler framover
    left(120)           # drei 120 grader venstre
    forward(200)  
    left(120) 
    forward(200)
    end_fill()
    
    time.sleep(10)
