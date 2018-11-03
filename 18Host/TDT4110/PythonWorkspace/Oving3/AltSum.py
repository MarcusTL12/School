import ConsoleUtil as cu



def a():
    n = cu.cin_I("n = ")

    s = 0
    sgn = 1

    for i in range(1, n + 1):
        s += sgn * i ** 2
        sgn *= -1

    print("Sum = " + str(s))


def b():
    k = cu.cin_I("k = ")

    s = 0
    last_s = 0
    sgn = 1
    n = 1

    while k >= s:
        last_s = s
        s += sgn * n ** 2
        sgn *= -1
        n += 1
    
    print("Sum før sum > k = " + str(last_s) + ". n = " + str(n - 2))
