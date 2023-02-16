# from polygon.polygon import Polygon
from square.square import Square
from rectangle.rectangle import Rectangle
from pentagon.pentagon import Pentagon

# p = Polygon(1,2)
# print(p)

print("Square areas and perimeter")
s=Square(3)
s.Area()
s.Perimeter()

print("\n")

print("Rectangle areas and perimeter")
r=Rectangle(3,6)
r.Area()
r.Perimeter()

print("\n")

print("Pentagon areas and perimeter")
p=Pentagon(3,6,4)
p.Area()
p.Perimeter()