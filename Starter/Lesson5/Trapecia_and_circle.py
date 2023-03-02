import math


def s_trap(bas1, bas2, left, right):
    return bas1 + bas2 + left + right


def perimetr(bas1, bas2, height):
    return (bas1 + bas2) * height / 2


def circle(radius):
    return 2 * math.pi * radius


def layer(radius):
    return 4 / 3 * math.pi * radius ** 2


value1 = int(input("\nSelect the action you want to perform:\n 1. Determining the perimeter of the trapezoid."
                   "\n 2. Determining the area of the trapezoid.\n 3. Determining the circumference of a circle."
                   "\n 4. Determining the volume of the sphere.\n 5. Completion of the program.\n"))

while True:
    if value1 == 1:
        sid1 = float(input("lower base: "))
        sid2 = float(input("upper base: "))
        sid3 = float(input("left side: "))
        sid4 = float(input("right side: "))
        print("The perimeter of the trapezoid: ", s_trap(sid1, sid2, sid3, sid4))
    elif value1 == 2:
        sid1 = float(input("lower base: "))
        sid2 = float(input("upper base: "))
        h1 = float(input("enter the height: "))
        print("The area of the trapezoid", perimetr(sid1, sid2, h1))
    elif value1 == 3:
        rad = float(input("enter the radius: "))
        print("The circumference of a circle", round(circle(rad), 2))
    elif value1 == 4:
        rad = float(input("enter the radius: "))
        print("The volume of the sphere", round(layer(rad), 2))
    elif value1 == 5:
        print("The program is completed.")
        break
    else:
        print("Enter a value from 1 to 5")
    value1 = int(input("\nSelect the action you want to perform:\n 1. Determining the perimeter of the trapezoid."
                       "\n 2. Determining the area of the trapezoid.\n 3. Determining the circumference of a circle."
                       "\n 4. Determining the volume of the sphere.\n 5. Completion of the program.\n"))
