import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())


def longer_line(x1, y1, x2, y2, a1, b1, a2, b2):
    line_len_1 = math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
    line_len_2 = math.sqrt(((a2 - a1) ** 2) + (b2 - b1) ** 2)
    if line_len_1 > line_len_2:
        distance1 = (x1 ** 2) + (y1 ** 2)
        distance2 = (x2 ** 2) + (y2 ** 2)
        if distance1 < distance2:
            return print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
        else:
            return print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
    else:
        distance_a = (a1 ** 2) + (b1 ** 2)
        distance_b = (a2 ** 2) + (b2 ** 2)
        if distance_a < distance_b:
            return print(f"({math.floor(a1)}, {math.floor(b1)})({math.floor(a2)}, {math.floor(b2)})")
        else:
            return print(f"({math.floor(a2)}, {math.floor(b2)})({math.floor(a1)}, {math.floor(b1)})")


longer_line(x1, y1, x2, y2, a1, b1, a2, b2)
