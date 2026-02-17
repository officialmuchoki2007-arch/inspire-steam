# Name : Stacy Muchoki
# Date : 17/02/2026
# Program to perform arithmetic operations

f_number = 12
s_number = 34

sum_numbers = f_number + s_number
diff_numbers = f_number - s_number
product_numbers = f_number * s_number
quotient_numbers = f_number / s_number

print("the sum is %d"%sum_numbers)
print("the quotient is %0.2f"%quotient_numbers)

#modulus is remainder
print(7%5)

# even and odd numbers
for x in range(0,21):
    if( x%2 == 1):
        print(f"{x} odd")

    elif( x%2 == 2):
        print(f"{x} is even")
    
    
