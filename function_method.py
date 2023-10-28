# function and method

def add(a,b):     #function
    return a + b

class Calculator:
    def add(self, a, b):    #method - inside the class
        return a + b
    

# Class -> user defined data type

class Student:
    def __init__(self, name, roll_num, mark):   # __init__ -> constructor -> only create object it call. not need to call separate
        self.name = name
        self.roll_num = roll_num
        self.mark = mark

calc = Calculator()
print(calc.add(10, 29))

# not call but produce output for init
s1 = Student("ezhil", 44, 500)
print(s1.name)
print(s1.roll_num)
print(s1.mark)


# class variable ----> avoid redundency and less memory

class Product:
    discount = 10  # class variable
    def __init__(self, name, price):
        self.name = name   # self.name --> instance variable
        self.price = price

    def discount1(self):
        dis_amt = (self.price * self.discount) / 100
        return (int(self.price) - int(dis_amt))
    
p1 = Product("Phone" , 100)
print(p1.discount1())

p2 = Product("Fridge" , 100)
p2.discount = 5       # separate we can give
print(p2.discount1())

p3 = Product("Phone" , 100)
print(p3.discount1())

