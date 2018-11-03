import ConsoleUtil as cu

NUM_MOL = 6.022e23

def a():
    stoff = input("Hva stoff har du?: ")
    mass_mol = cu.cin_F("Hva er molmassen til " + stoff + "? ")
    mass_stoff = cu.cin_F("Hvor mye " + stoff + " har du [g]: ")
    print("Du har " + format(NUM_MOL * mass_stoff / mass_mol, '.3e') + " molekyler " + stoff)


NUM_MEL = 8.25e19

def b():
	mel_listn = cu.cin_I("Hvor mange 10-toners melodier har du hørt? ")
	print("Du har hørt " + format(100 * mel_listn / NUM_MEL, '.2e') + " % av alle 10-toners melodier")