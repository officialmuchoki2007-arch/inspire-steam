# Name : Stacy Muchoki
# Date : 23/02/2026
# Program to show inheritance in Python 


class Animal():
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self, weight):
        weight = 1.1 * self.weight
        print(f"The {self.species} has grown to {weight} kg.")

    def eat(self, food):
        print(f"The animal eats {food}")



class Dog(Animal):
    def __init__(self, color, weight, breed):
        super().__init__(species,weight,food)
        self.height = height
        self.breed = breed

    def barks(self):
        print(f"The dog says woof woof")


class Horse(Animal):
    def __init__(self, color, weight, breed):
        self.color = color
        self.weight = weight
        self.breed = breed

    def grow(self, weight):
        weight = 1.1 * self.weight
        print(f"The {self.species} has grown to {weight} kg.")

    def eat(self):
        print(f"The horse says neigh neigh")