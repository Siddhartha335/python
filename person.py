# class Person:
#     def cry(self):
#         print("Crying")
    
#     def __init__(self,gender):
#         self.sex = gender

#     def __str__(self):
#         return "Person is a {}".format(self.sex)

#     # def __repr__(self):


# a= Person("Male")
# b= Person("Female")
# # a.cry()
# # print(a.sex)

# print(a)
# print(b)



# Inheritanace-example

# class Person:
#     def __init__(self,firstname,lastname):
#         self.fname=firstname
#         self.lname=lastname

#     def printName(self):
#         print(self.fname,self.lname)

# # c = Person("Sid","Raut")
# # c.printName()

# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)


# s=Student("Sid","Raut")
# s.printName()

        
# class Person:
#     name=""
#     sex=""

#     def eat(self):
#         print("I can eat!")

# class Homo(Person):
#     def display(self):
#         print("My name is {}".format(self.name))
#         print("My gender is {}".format(self.sex))

# a = Homo()
# a.eat()
# a.name="Sid"
# a.sex="Male"
# a.display()