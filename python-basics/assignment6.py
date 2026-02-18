# Name : Stacy Muchoki
# Date : 17/02/2026
# Program to display Diamond using *, Triangle
# Program to solve quadratic equation


rows = 5 

# Upper half of the diamond
i = 1
while i <= rows:
    j = 1
    
    while j <= (rows - i):
        print(" ", end="")
        j += 1
    
    k = 1
    
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    
    print() 
    i += 1


# Lower half of the diamond
i = rows - 1
while i >= 1:
    j = 1
    
    while j <= (rows - i):
        print(" ", end="")
        j += 1
    
    k = 1
    
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    
    print() 
    i -= 1


i = 1
while i <= rows:
    j = 1
    
    while j <= (rows - i):
        print(" ", end="")
        j += 1
    
    k = 1
    
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    
    print() 
    i += 1









