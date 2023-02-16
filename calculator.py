# class Calculator:
#     def add(self,a,b):
#         print(a+b)

#     def sub(self,a,b):
#         return a-b

#     def mul(self,a,b):
#         return a*b

#     def div(self,a,b):
#         return a/b


# c=Calculator()
# print("Addition is: " ,c.add(1,2))
# print("Addition is: " ,c.sub(1,2))
# print("Addition is: " ,c.mul(1,2))
# print("Addition is: " ,c.div(1,2))

# a= int()
# print(type(a))

# c=Calculator() 
# print(type(c))


# class Calculator:
#     def add(sef,*args):
#         sum=0
#         for i in args:
#             sum+=i
#         return sum


# c= Calculator()

# print("The sum is", c.add(1,2,3,4,5,6,7,8,9,10))


# class AddCalculator:
#     def __init__(self): #Dunders INIT or Python class constructor
#         print("Hello from  add constructor!")

#     def add(self,a,b):
#         # print("Hello from add calculator!")
#         print(a+b)
    
# class SubCalculator:
#     # def __init__(self): #Dunders INIT or Python class constructor
#     #     print("Hello from constructor!")

#     def sub(self,a,b):
#         print(a-b)

# class MulCalculator:
#     # def __init__(self): #Dunders INIT or Python class constructor
#     #     print("Hello from constructor!")

#     def mul(self,a,b):
#         print(a*b)

# class DivCalculator:
#     # def __init__(self): #Dunders INIT or Python class constructor
#     #     print("Hello from constructor!")

#     def div(self,a,b):
#         if b==0:
#             print("Denominator is zero!")
#         else:
#             print(a/b)

# It is inheriting features and properties of add,sub,mul and div
# class Calculator(AddCalculator,SubCalculator,MulCalculator,DivCalculator):
#     def __init__(self):
#         print("Hi from main calcualtor!")

# c=Calculator()
# c.add(1,3)
# c.sub(3,1)
# c.mul(2,4)
# c.div(1,0)

# c= AddCalculator();
# c.add(1,2)
# x=SubCalculator();
# x.sub(5,1)
# y=MulCalculator();
# y.mul(3,6)
# z=DivCalculator();
# z.div(4,0)





# class PolyAdditionCalculator(AddCalculator):
#     def __init__(self):
#         print("HI from PolyAdditionCalculator!")

#     # Method overloading
#     def add(self,*args,binary=False):
#         if binary and len(args)==2:
#             return super().add(args[0],args[1])
#         else:
#             sum=0
#             for i in args:
#                 sum+=i
#             return sum
        
# c = PolyAdditionCalculator()
# print(c.add(1,2,binary=True))

# Abstraction,Inheritance and Polymorphism
# Create a base class Polygon with basic features and properties like no of sides, write init and str dunders to initialize
# and print info on the object

#Define methods like area,volume,perimeter etc
#inherit the base class to create like SQUARE, RECTANGLE, QUADRILATERAL,PENTAGON,HEXAGON etc with respective properties and methods

class Polygon():
    def __init__(self,no_of_sides):
      self.no_of_sides = no_of_sides
      print("You have choosen {} sides".format(no_of_sides))

    def area(self,length,breadth):
       res = (length*breadth)
       print("The area is", res)

    def volume(self,length,breadth,height):
       res = length*breadth*height
       print("The volume is", res)

class Square(Polygon):
    def __init__(self,no_of_sides):
      self.no_of_sides = no_of_sides
      print("You have choosen {} sides of square".format(no_of_sides))

class Rectangle(Polygon):
    def __init__(self,no_of_sides):
      self.no_of_sides = no_of_sides
      print("You have choosen {} sides of rectangle".format(no_of_sides))

class Triangle(Polygon):
    def __init__(self,no_of_sides):
      self.no_of_sides = no_of_sides
      print("You have choosen {} sides of triangle".format(no_of_sides))

    def area(self, length, breadth):
       res= 1/2 * (length*breadth)
       print("The area is", res)

    def volume(self, length, breadth, height):
       res = 1/2 * (length*breadth*height)
       print("The area is", res)
       
print("Square areas and volumes")
s=Square(4)
s.area(4,5)
s.volume(4,5,6)

print("Rectangle areas and volumes")
r=Rectangle(4)
r.area(2,4)
r.volume(3,4,7)

print("Triangle areas and volumes")
t=Triangle(3)
t.area(3,8)
t.volume(4,6,2)





       
       