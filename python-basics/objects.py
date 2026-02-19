# Name : Stacy Muchoki
# Date : 19/02/2026
# Program to demonstrate objects in Python

class Human:
    # First we define attributesof a human bieng
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # Now we create a contsructor for the class
    # The constructor will be used to create objects of the class human
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_story(self):
        print(f"I am a {self.name}. Here is a story")
        print("Once upon a time, there was a human being who lived in a small village. He was very kind and loved by everyone in the village. One day, he decided to go on an adventure to explore the world. He traveled to many different places and met many different people. He had many exciting experiences and learned a lot about the world. In the end, he returned to his village and shared his stories with everyone. The end.")

# Create the objects of the class human
stacy = Human("Stacy", 19)
sean = Human("Sean", 20)

# Let the humans tell their stories
stacy.tell_story()
stacy.age
print(f"stacy's age is {stacy.age}")

# Modify one of the objects without affecting the other object
#b4 modification
print(f"Sean's city is {sean.city}")
print(f"Stacy's city is {stacy.city}")
#modification
sean.city = "Mombasa"
print(f"Sean's city is {sean.city}")
print(f"Stacy's city is {stacy.city}")



