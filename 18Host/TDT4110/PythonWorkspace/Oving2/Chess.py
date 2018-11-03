

def ab():
    x_pos = 1
    y_pos = 1

    valid_input = False

    while not valid_input:
        pos = input("Posisjon: ")
        x_pos = ord(pos[0].lower()) - 96
        if x_pos < 1 or x_pos > 8:
            print("X verdi out of bounds; Prøv igjen:")
            continue
        
        try:
            y_pos = int(pos[1])
            if y_pos < 1 or y_pos > 8:
                print("Y verdi out of bounds; Prøv igjen:")
                continue
        except:
            print("Y verdi ikke tallverdi; Prøv igjen:")
            continue

        valid_input = True

    x_sgn = ((x_pos - 96) % 2) * 2 - 1
    y_sgn = (y_pos % 2) * 2 - 1
    print("Svart" if (x_sgn * y_sgn) == 1 else "Hvit")


