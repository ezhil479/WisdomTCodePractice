# formula for circle area = pi * r * r
# circumference => 2 * pi * r

class Circle:
    def __init__(self,radius, pi):   # self -> object reference
        self.radius = radius
        self.pi = pi
        print("This is circle area and circumference")

    def area(self):
        area_val = self.pi * self.radius * self.radius
        print (area_val)
    def circumference(self)    :
        circum_val = 2 * self.pi * self.radius
        print (circum_val)
        
Cir = Circle(2, 3.14)   # create object
Cir.area()
Cir.circumference()



# class variable
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area_value = Circle.pi * self.radius * self.radius
        return area_value
    def circumference(self):
        circum_value = 2 * Circle.pi * self.radius
        return circum_value

c = Circle(4)
print(c.area())
print(c.circumference())
print(c.__dict__)