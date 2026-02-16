# Name : Stacy Muchoki
# Date : 16/02/2026
# Program to calculate factorials of numbers

number = int(input("enter the number :"))

factorial = 1 # initialize factorial = 1

for x in range(1,number + 1):
    factorial*=x
print(f"{number}! = {factorial}")

