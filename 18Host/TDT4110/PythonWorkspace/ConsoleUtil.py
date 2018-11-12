

def cin_I(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except Exception:
            print("Input not an integer. Try again: ")


def cin_F(s: str) -> float:
    while True:
        try:
            return float(input(s))
        except Exception:
            print("Input not a number. Try again: ")

