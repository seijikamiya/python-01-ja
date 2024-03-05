def add(a, b):
    if type(a) in [float, int] and type(b) in [float, int]:
        return a+b
    else:
        return "bad input"


def subtract(a, b):
    if type(a) in [float, int] and type(b) in [float, int]:
        return a-b
    else:
        return "bad input"


def multiply(a, b):
    if type(a) in [float, int] and type(b) in [float, int]:
        return a*b
    else:
        return "bad input"


def divide(a, b):
    if type(a) in [float, int] and type(b) in [float, int]:
        if b != 0:
            return a/b
        else:
            return "Cannot divide by zero"    
    else:
        return "bad input"