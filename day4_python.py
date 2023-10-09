# 1. Dictionary operations
price_list = {"apple": 30, "orange": 20, "banana": 10, "pomegranate":40}

print(price_list.keys())
print(price_list.values())

# 2. create empty dictionary and add key,values
price_list = {} 

print(price_list)

price_list["apple"] = 50
price_list["cherry"] = 70

print(price_list)

# 3. update
price_list = {"apple": 30, "orange": 20, "banana": 10, "pomegranate":40}
print(price_list)

price_list["cherry"] = 15  # add
price_list["banana"] = 55    # update
print(price_list)

# 4. delete using del keyword
price_list = {"apple": 30, "orange": 20, "banana": 10, "pomegranate":40}
print(price_list)

del price_list["apple"]  # use []
print(price_list)

#5. delete using pop keyword
price_list = {"apple": 30, "orange": 20, "banana": 10, "pomegranate":40}
print(price_list)
price_list.pop("banana")   # use ()
print(price_list)


# 6. check if fruit exit in dict
price_list = {"apple": 30, "orange": 20, "banana": 10, "pomegranate":40}

if "apple" in price_list:
    print("Available")
else:
    print("This fruit not available")


# 7. check pass or fail
marks = {"Kumar":45,"Priya":78,"Raja":90,"Ravi":35,"Mani":62}

for name,mark in marks.items():
    if mark > 50:
        print(name,mark)

# 8. if fail - give grace mark 10

marks = {"Kumar":45,"Priya":78,"Raja":90,"Ravi":35,"Mani":62}

for name,mark in marks.items():
    if mark < 50:
        marks[name] = mark + 10

for name,mark in marks.items():
    if mark < 50 :
        print(f"{name} is fail..")



marks = {"Kumar":45,"Priya":78,"Raja":90,
          "Ravi":35,"Mani":62,"Vijay":28,
          "Rani":41,"Selvam":85,"Malar":55}

print (marks)


for name,mark in marks.items():
    if mark < 50:
        marks[name] = mark + 10

for name,mark in marks.items():
    if mark < 50:
        print (f"{name} is fail")


# 9. del

class_6th = {"Kumar":45,"Priya":78,"Raja":90,
          "Ravi":35,"Mani":62,"Vijay":28,
          "Rani":41,"Selvam":85,"Malar":55}

for name,mark in class_6th.copy().items():
    if mark < 50:
        del class_6th[name]
print(class_6th)

# 10. print fail and pass students in a class
class_6th = {"Kumar":45,"Priya":78,"Raja":90,
          "Ravi":35,"Mani":62,"Vijay":28,
          "Rani":41,"Selvam":85,"Malar":55}
fail_student = {}
pass_student = {}

for name, mark in class_6th.items():
    if mark < 50:
        fail_student[name] = mark
    else:
        pass_student[name] = mark

print(f"Fail student: ",fail_student)
print(f"Pass student: ",pass_student)

# 11. while loop
i = 0

while i != 4:
    print("hi")
    i += 1
print("loop outside")    


shop = {"apple":40,"pomegranate":30,"orange":15,"banana":10}

# quantity = int(input("Enter quantity: "))
while True:
    fruit = input("Enter fruit: ")
    if fruit == "quit":
        break
    if fruit in shop:
        print(f"{fruit} is available...")
    else:
        print(f"{fruit} not available.")
print("Thank you")
##
 
shop = {"apple":40,"pomegranate":30,"orange":15,"banana":10}

fruit = ''

while fruit != "quit":
    fruit = input("Enter the fruit name :")
    if fruit in shop:
        print ("Yes its available")
    else:
        print ("No its not available")


print ("Thank you")


# total price find
shop = {"apple":40,"pomegranate":30,"orange":15,"banana":10}

fruit = ''
total = 0

while fruit != "quit":
    fruit = input("Enter the fruit name :")
    if fruit == "quit":
        continue
    quantity = int(input("Enter the quantity :"))
    temp_total = shop[fruit] * quantity
    total = total + temp_total


print (f"Please pay Rs.{total}")



shop = {"apple":40,"pomegranate":30,"orange":15,"banana":10}

fruit = ''
total = 0

while fruit != "quit":
    if fruit:
        quantity = int(input("Enter the quantity :"))
        temp_total = shop[fruit] * quantity
        total = total + temp_total
    fruit = input("Enter the fruit name :")


print (f"Please pay Rs.{total}")


# set
set1 = {'a','b','c','d'}
print(set1)

set1.add('python')
set1.add('a')

print(set1)
#
for value in set1:
    print(value)
    
# set operations
english = {"kumar","priya","Ravi","John","Rani"}
hindi = {"vijay","John","khan","sharma","priya"}

print(english - hindi)
print( hindi - english)
print(english ^ hindi)
print(english | hindi)
print(english & hindi)


list1 = [5,3,7,4,9,10,1,7]
print("List1 - ",list1)

var = sorted(list1)

print("List1 sorted - ", var)
print(list1)


list2 = [None] * 10
print(list2)
list2[4] = "Ezhil"
list2[8] = "mahith"
list2[3] = "lokesh"
list2[1] = "sanjith"
print(list2)
 

a = [(2,3),(5,2),(8,1)]

b = dict(a)
print(type(a))
print(type(b))
print(b)

result = {"Kumar":45,"Priya":78,"Raja":90,"Ravi":35,"Mani":62}
print(result)
list3 = result.keys()
print(list3, type(list3))

list4 = result.values()

print(list4, type(list4))
