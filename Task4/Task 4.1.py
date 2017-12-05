class Point:
    count=int()
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.count+=1
    def __add__(self, point):
        point.x=self.x + point.x
        point.y=self.y + point.y
        return point

p1 = Point(4,5)
p2 = Point(5,4)
p3 = p2.__add__(p1)
print(p3.x, p3.y)
