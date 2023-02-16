class Polygon():
    def __init__(self,*args):
        self.args=args
        
        
    def __str__(self):
        if len(self.args)==1:
            return("It is a square")
            # print("The total side of the polygon is {}".format(len(args)))
        elif len(self.args)==2:
            return("It is a rectangle")
        elif len(self.args)==3:
            return("It is a pentagon")
        elif len(self.args)==4:
            return("It is a hexagon!")
            # print("The total side of the polygon is {}".format(len(args)))
        
    def Area(self):
        pass

    def Perimeter(self):
        pass
