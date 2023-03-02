import math

def s_circle(r):
    return 2 * math.pi * r


def s_square(a):
    return a ** 2


def s_rectangle(a, b):
    return a * b


def s_triangle(a, b):
    return 0.5 * a * b


def v_layer(r):
    return 4 / 3 * math.pi * r ** 3


def v_cube(a):
    return a ** 3


def v_paral(a, b, c):
    return a * b * c


def v_cone(r, h):
    return 1 / 3 * math.pi * r ** 2 * h

