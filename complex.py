a = 0
b = 0
c = 0
d = 0


def init(a, b, c, d):
    global x, y
    x = complex(a, b)
    y = complex(c, d)


def return_x():
    return x

def return_y():
    return y

def do_sum():
    return x + y

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
        return  do_sub()
    elif action == '*':
        return do_mult()
    elif action == '/':
        return do_div()