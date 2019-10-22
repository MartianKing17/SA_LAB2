import init
import numpy as np
import matplotlib.pyplot as plt


def get_x():
    #Convert const number x to vector x
    x_value = float(input("Input x: "))
    x = np.zeros((3, 1))
    for i in range(3):
        x[i] = x_value

    return x


def get_value():
    value = []
    var = float(input("Input a1: "))

    if var >= 1 and var <= 10:
        value.append(var)
    else :
        raise Exception

    var = float(input("Input a2: "))

    if var >= 1 and var <= 10:
        value.append(var)
    else:
        raise Exception

    var = float(input("Input t0: "))
    value.append(var)
    var = float(input("Input q: "))
    value.append(var)
    return value


def var_1(t, f, g, x):
    x_n = []
    l = float(input("Enter l2: "))
    l = init.init_l(l2=l)

    for i in range(len(t)):
        x = init.calculate_x(f, g, x, l)
        x_n.append(x)

    return x_n


def var_2(t, f, g, x):
    x_n = []
    l = float(input("Enter l3: "))
    l = init.init_l(l3=l)
    k0 = float(input("Input k0: "))
    k = 0

    for i in range(len(t)):
        x = init.calculate_x(f, g, x, l)
        x_n.append(x)

    return x_n


def choice_variant():
    variant = float(input("Input variant: "))

    if variant == 1:
        func = var_1
    elif variant == 2:
        func = var_2
    else:
        raise ValueError

    return func


def draw(t, y):
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.grid()

    for i in range(len(y)):
        plt.plot(range(len(t)), y[i])
        text = "x" + str(i)
        plt.legend(('x1', 'x2', 'x3'))

    plt.show()


def main():
    try:
        value = get_value()
    except Exception:
        print("a1 and a2 must be a1 >= 1 && a2 >= 1 && a1 =< 10 && a2 =<10")
        return 0

    x = get_x()
    t = np.arange(0, 10 + value[2], value[2])
    a = init.init_a(value[0], value[1])
    f = init.calculate_f(a, value[2], value[3])
    g = init.calculate_g(f, a)

    try:
     func = choice_variant()
    except ValueError:
        print("Error")
        return 0

    x = func(t, f, g, x)
    y = init.init_y(x, t)
    draw(t, y)


main()
