from fractions import Fraction

x = 0
y = 0

def init(a, b, c, d):
    global x
    global y
    x = Fraction(a) / Fraction(b)
    y = Fraction(c) / Fraction(d)


def return_x():
    return x

def return_y():
    return y

def do_sum():
    return x + y

def do_sub():
    return x - y

def do_sub():
    return x - y

def do_mult():
    return x * y

def do_div():
    return x / y

def do_it(action):
    if action == '+':
        return do_sum()
    elif action == '-':
        return do_sub()
    elif action == '*':
        return do_mult()
    elif action == '/':
        return do_div()

