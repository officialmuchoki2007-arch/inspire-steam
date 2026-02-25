# Name : Stacy Muchoki
# Date : 24/02/2026
# Program to demonstrate file input/output operations in Python


# Create a new file
new_file = open("student_data.txt", "r+")



# Write to the file
new_file.write("{student_name: Stacy Muchoki , ID: 123456 , email: stacy@gmail.com}")



# Read from the file
new_file = open("student_data.txt", "r+")

data = new_file.read()
print(data)

new_file.close()


# Delete the file
#us os module
import os
os.remove("remove.txt")



#delete folder
os.rmdir("folder_name")







# Delete folder