class Point:
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")


    def draw(self):
        print("draw")


'''points = Point(10 , 20)
print(points.x)'''


points = Point
points.x = 13

print(points.x)
