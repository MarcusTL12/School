import ConsoleUtil as cu


def fib_at(k: int) -> int:
    if k <= 0:
        return 0
    elif k == 1:
        return 1
    
    a = 0
    b = 1
    
    if k % 2 == 0:
        k -= 1
        a = 1
        b = 1

    for i in range((k - 1) // 2):
        a = a + b
        b = a + b
    
    return b


def fib_sum(k: int) -> int:
    if k <= 0:
        return 0
    elif k == 1:
        return 1
    
    a = 0
    b = 1
    
    s = 1

    if k % 2 == 0:
        k -= 1
        a = 1
        b = 1
        s = 2

    for i in range((k - 1) // 2):
        a = a + b
        s += a
        b = a + b
        s += b
    
    return s


def fib_list(k: int) -> list:
    if k <= 0:
        return []
    elif k == 1:
        return [0]

    res = [0] * k
    res[1] = 1

    if k == 2:
        return res
    
    for i in range(2, k):
        res[i] = res[i - 2] + res[i - 1]

    return res


def a():
    k = cu.cin_I("Hvilket fibonacci tall vil du ha? ")
    print(fib_at(k))


def b():
    k = cu.cin_I("Hvor mange fibonacci tall vil du legge sammen? ")
    print(fib_sum(k))


def c():
    k = cu.cin_I("Hvor mange fibonacci tall vil du ha? ")
    print(fib_list(k))
