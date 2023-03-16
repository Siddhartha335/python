from person.person import Person
import datetime
today = datetime.date.today()
year = today.year

class Male(Person):
    # def __init__(self,gender):
    #     self.gender=gender

    # def __str__(self,gender):
    #     self.sex = gender
    #     print("My gender is {}".format(self.sex))

    gender="Male"
    money=18000

    def displayInfo(self):
        name=input("Enter your name:")
        print("Your name is",name)
        print("Your gender is",self.gender)
        
    def calculateAge(self):
        dob=input("Enter your date of birth in yyyy-mm-dd format:")
        print("Your date of birth is",dob)
        intDob = int(dob[0:4])
        print("Your current age is {}".format(year-intDob))

    def salary(self):
        print("Your starting salary is",self.money)

    def incrementSalary(self):
        additionalSalary = int((0.1 * self.money) + self.money)
        print("Your incremented salary after one year is {}".format(additionalSalary))
        