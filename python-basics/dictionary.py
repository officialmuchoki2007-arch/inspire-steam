# Name : Stacy Muchoki
# Date : 18/02/2026
# Program to show dictinary in python

car = {"Model": "Toyota", 
        "Year": 2020, 
        "Color": "Red"}
print(car)
print(car["Model"])
print(car["Year"])
print(len(car))

students = {"Hope": 85, 
            "John": 90, 
            "Emily": 78}
for key in students: 
    print(key)

for val in students.values(): 
    print(val)  

students = dict(Hope=85, 
                John=90, 
                Emily=78)
print(students)