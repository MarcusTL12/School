import ConsoleUtil as cu


def roundUp(n, d):
    return int(n * (10 ** d) + 0.5) / (10 ** d)


def a():
    n = cu.cin_F("Skriv et desimaltall: ")
    d = cu.cin_I("Antall desimaler: ")
    print("Avrundet: " + str(roundUp(n, d)))


def roundcorr(n, d):
    tol = 10 ** (- 18)
    n *= 10 ** d
    if abs(n % int(n) - 0.5) < tol:
        n = int(n)
        if n % 2 != 0:
            n += 1
    else:
        n = int(n + 0.5)

    return n / (10 ** d)


def b():
    n = cu.cin_F("Skriv et desimaltall: ")
    d = cu.cin_I("Antall desimaler: ")
    print("Avrundet: " + str(round(n, d)))
    print("Avrundet korrigert: " + str(roundcorr(n, d)))


def c():
    prefixes = ["von", "van", "de", "di"]
    suffixes = ["jr", "sr", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

    name = input("What's your name? ")
    name_list = name.split()
    surname = ""
    add_names = False
    amt_prefixes = 0
    for i in range(1, len(name_list) - 1):
        if name_list[i].lower() in prefixes and not add_names:
            add_names = True
        
        if add_names and not (name_list[i].lower() in suffixes):
            surname += name_list[i] + " "
            amt_prefixes += 1
    
    if not name_list[len(name_list) - 1].lower() in suffixes:
        if len(name_list) > 2 and amt_prefixes > 1:
            surname += name_list[len(name_list) - 2] + " "
        surname += name_list[len(name_list) - 1]

    print("The name is " + surname + ", " + name)
