class Point():
    # Method called everytime I try to create point
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
p = Point(2,8)
print(p.x)
print(p.y)
        