# Name : Stacy Muchoki
# Date : 18/02/2026
# Program to demonstrate list operations in Python

# Creating a list of friends
friends = ["Rachael", "Ross", "Monica", "Chandler", "Joey", "Phoebe"]
print(friends)

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Gunther")
print(friends)

new_friends = ["Sean", "Spencer", "Poppy", "Emily", "Charlie"]
print(len(new_friends))

# New list of students
students = friends + new_friends
print(students)

students.pop()
print(students)

students.insert(5, "Peter")
print(students)
students.insert(9, "Valarie")
print(students)

students.extend(["Alice"])
print(students)

students.remove("Sean")
print(students)

new_students = students.copy()
print(new_students)