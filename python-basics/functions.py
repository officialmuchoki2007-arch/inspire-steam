# Name : Stacy Muchoki
# Date : 19/02/2026
# Program to display functions in python

def cook_egg():
    oil = True
    pan = True
    moto = True
    eggs = 2

    print(f"The pan is hot {pan}, and the fire is {moto}, add {oil} amount of oil, and crack {eggs} eggs into the pan.")
cook_egg()

print("here is statement 1")

print("here is statement 2")

cook_egg()

print("here is statement 3")

# Ride fare creating a function

def create_fare(route, distance, is_rush_hour):

    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5

    print(f"The fare for {route} is {fare}.")

    return fare

returned_fare = create_fare("Juja_Allsops", 7, True)
print(f"The returned fare is: {returned_fare}")

# Passing a list as a parameter to a function

def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")
all_interests = {"Watching movies", "Traveling", "Cooking", "Dancing"}
write_all_interests(all_interests)


