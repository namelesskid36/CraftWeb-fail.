#----------------------------------------------------------------------------------------#
# class Room:
#     a = int(input("Length: "))
#     b = int(input("Breadth: "))
#     c = int(input("Height: "))


#     def calculate_area(self, celling):
#         self.celling = celling
#         return self.a*self.b

#     def volume(self):
#         return self.a *self.b*self.c

# section_one = Room()
# print("The area of the object is: ", section_one.calculate_area(celling = 10))
# print("The Volume of the object is: ", section_one.volume())

#----------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------#
class calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.addition = self.num1 + self.num2
        self.subtraction = self.num1 + self.num2
        self.multiplication = self.num1 + self.num2
        self.division = self.num1 + self.num2

    def add(self, *args, **kwargs):
            total = 0
            for n in args:
                total += n
            return total
    
    def subtraction(self, *args, **kwargs):
            total = [0]
            for n in args[1:]:
                total -= n
            return total
    
    # def multiply(self, num1, num2):
    #         return num1*num2
    
    # def division(self, num1, num2):
    #         return num1/num2

calc = calculator(1,2)
print(calc.addition)
print(calc.add(1,2,3))
print(calc.subtraction(1,2))