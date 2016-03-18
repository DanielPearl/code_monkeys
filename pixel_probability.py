def pixel_probability(length,width):
    print (256 * 256 * 256 * length * width)

class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def overlap(self, other):
        if self.x < other.x + other.w and self.x + self.w > other.x and self.y < other.y + other.h and self.y + self.h > other.y:
            return True
        elif other.x < self.x + self.w and other.x + other.w > self.x and other.y < self.y + self.h and other.y + other.h > self.y:
            return True
        else:
            return False

a = Rectangle(1,-3,4,2)
b = Rectangle(4,-6,2,4)

print(a.overlap(b))
