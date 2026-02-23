# Name : Stacy Muchoki
# Date : 23/02/2026
# Program to show cars module in Python


class Car():
    #attributes of a car
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    #print the details of the car
    def print_details(self):
        print(f"The car is a {self.color} {self.make} {self.model} from the year {self.year}.")
        

#create an object of the car class
my_car = Car("Toyota", "Corolla", "Red", 2020)
dads_car = Car("Honda", "Civic", "Blue", 2018)
my_car.print_details()
dads_car.print_details()