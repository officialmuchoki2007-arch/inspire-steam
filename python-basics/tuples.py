# Name : Stacy Muchoki
# Date : 18/02/2026
# Program to show tuples in python

# Tuples of fruits
fruits = ("Mango", "Banana", "Pineapple", "Watermelon", "Grapes")
print(len(fruits))
print(fruits[0])
print(fruits[3])
print(fruits[-1])
print(fruits[-5])

#fruits.append("Strawberry")- This will raise an error because tuples are immutable

fruits_list = list(fruits)
fruits_list.append("Strawberry")
print(fruits_list)