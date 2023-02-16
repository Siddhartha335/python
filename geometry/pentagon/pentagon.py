from polygon.polygon import Polygon

class Pentagon(Polygon):
    def __init__(self, *args):
        self.args = args
        self.length = self.args[0]
        self.breadth = self.args[1]
        self.apothem = self.args[2]

    def __str__(self):
        if len(self.args) < 3:
            return("Pentagon requires three arguement ")
        elif len(self.args) > 3:
            return("Improper pentagon initialization")
        else:
            return("Perfect pentagon initialization")
        
    def Area(self):
        perimeter = 5 * self.length *self.breadth
        print("Area of the pentagon is {}".format(0.5*(perimeter*self.apothem)))

    def Perimeter(self):
        print("Perimeter of the pentagon is {}".format(5*(self.length)))