from polygon.polygon import Polygon

class Square(Polygon):
    def __init__(self, *args):
        self.args = args
        self.length = self.args[0]

    def __str__(self):
        if len(self.args)==0:
            return "Square uninitialized"

        elif(len(self.args))>1:
            return("Improper Square initialization")
        
        else:
            return "Square initialized"
        
    def Area(self):
        print("Area of the square is {}".format(self.length*self.length))

    def Perimeter(self):
        print("Perimeter of the square is {}".format(self.length*4))