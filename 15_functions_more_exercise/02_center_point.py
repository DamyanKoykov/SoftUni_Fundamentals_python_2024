import math

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())


def closest_to_center(x1, y1, x2, y2):
    distance1 = (x1 ** 2) + (y1 ** 2)
    distance2 = (x2 ** 2) + (y2 ** 2)
    if distance1 > distance2:
        return print(f"({math.floor(x2)}, {math.floor(y2)})")
    else:
        return print(f"({math.floor(x1)}, {math.floor(y1)})")


closest_to_center(a1, b1, a2, b2)

