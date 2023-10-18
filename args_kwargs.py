"""# celcius to farenheit conversion program
def celcius_to_farenheit(celcius):                    # function definition - parameter
    farenheit = (9 / 5) * celcius + 32

    print("Farenheit value: ", farenheit)


celcius = int(input("Enter celcius value: "))
celcius_to_farenheit(celcius)                         # function call - arguments


#Formula = (9/5)* Celcius_Value + 32

# program has an error

def pass_fail(name, mark):
    if mark >= 50:
        print(f"{name} is pass....")
    else:
        print("Fail...")    

name = input("Enter name: ")
mark = int(input("Enter mark: "))

pass_fail(name, mark)
# or
pass_fail(mark, name)   # arg position based - so program error

# program has an error

def pass_fail(*args):
    if int(args[0] >= 50):  # int(args[1] >= 50) - is correct. *args also position based
        print("Pass")
    else:
        print("Fail")    
name = input("ENter name: ")
mark = int(input("Enter mark: "))

pass_fail(name, mark)


#   *args - tuple - datatype

def pass_fail(*student_detail):
    if int(student_detail[1] >= 50):
        print("Pass")
    else:
        print("Fail")    

name = input("Enter name: ")
mark = int(input("Enter mark: "))

pass_fail(name, mark)

#  **kwargs - keyword args   == key - value

def pass_fail(name, mark):
    if mark >= 50:
        print("Pass")
    else:
        print("Fail")

pass_fail(name = "Ezhil", mark = 50)


# ** kwargs - keyword arguments
#  **kwargs - dictionary data type
def my_func(**kids):
    print(type(kids))
    print("Lastname is: " + kids["lname"])
    print("location is: " + kids["location"])

my_func(fname = "Ezhil", lname = "loki", location = "kolar")


 # Default value
def my_country(country = "India"):
    print("my country is: " + country)

my_country()    
my_country("UK")
my_country("USA")
my_country()
my_country("Japan")
 """

# passing other parameters
def my_function(list1):
    for i in list1:
        print(i)
l1 = [1,2,3,4]
my_function(l1)


def function2(list2):
    return list2
name = input("name: ")
a = function2(name)
print(a)
