import ConsoleUtil as cu


def ab():
    RECIPIE = (
        ("sukker(g)", 400),
        ("smør(g)", 320),
        ("sjokolade(g)", 500),
        ("egg", 2),
        ("hvetemel(g)", 460)
    )
    amt_cookie = []
    more_cookies = True
    while more_cookies:
        n = cu.cin_I("Hvor mange kjeks vil du lage? ")
        amt_cookie.append(n)
        choice = input("Vil du lage flere kjeks? (y/n): ")
        if choice == 'y':
            print("Nice!")
        elif choice == 'n':
            print("Aww :(")
            more_cookies = False
        else:
            print("Tar det som et ja :D ")
    
    print("Antall kjeks: ", end="")
    for i in RECIPIE:
        print(i[0].rjust(20), end="")
    print("")

    for i in amt_cookie:
        print(str(i).ljust(14), end="")
        for j in RECIPIE:
            print(str(format(i * j[1] / 48, '.1f')).rjust(20), end="")
        print("")

    print("Kos deg med alle kjeksene. Husk å del ;)")
