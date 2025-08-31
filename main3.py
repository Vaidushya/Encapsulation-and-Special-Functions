class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
p1 = point(2, 3)
print(p1)

p2 = point(5, 6)
print(p2)

p3 = point(8, 9)
print(p3)
