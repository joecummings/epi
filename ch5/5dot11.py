class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def intersection(r1: Rectangle, r2: Rectangle) -> bool:
    if ((r1.x + r1.width) >= r2.x):
        if ((r1.y + r1.height) >= r2.y):
            return True
    return False


r_1 = Rectangle(20, 20, 20, 20)
r_2 = Rectangle(0, 0, 100, 100)
r_3 = Rectangle(50, 50, 10, 10)

assert intersection(r_1, r_2) == True
assert intersection(r_1, r_3) == False
assert intersection(r_2, r_3) == True
assert intersection(r_2, r_2) == True
