from polygon.polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, *args):
        self.args = args
        self.length = self.args[0]
        self.breadth = self.args[1]

    def __str__(self):
        if len(self.args) < 2:
            return("Rectangle requires two arguement ")
        elif len(self.args) > 2:
            return("Improper rectangle initialization")
        else:
            return("Perfect rectangle initialization")
        
    def Area(self):
        print("Area of the rectangle is {}".format(self.length*self.breadth))

    def Perimeter(self):
        print("Perimeter of the rectangle is {}".format(2*(self.length+self.breadth)))