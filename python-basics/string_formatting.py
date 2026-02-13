# Stacy Muchoki
# Date : 12/02/2026
# String formatting

# Get string length
sentence = "I am learning python"


string_length = len(sentence)

print(f"The length of the sentence is: {string_length}")
#splitting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])


#make everything uppercase
mpesa_code = "ubdh1234"

capitalized = mpesa_code.upper()

print("New mpesa code is: ", capitalized)

#make everythong lowercase
mpesa_code_2 = "UBFGTR343"

lowercase = mpesa_code_2.lower()

print("New mpesa_code is: ", lowercase)
# Replacing characters in a string

balance = "100kes"
amount_added = "50kes"

cleaned_balance = balance.replace("kes", "")

print("Cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("kes", "")

print("cleaned amount added: ", cleaned_amount_added)

#Answer
new_balance = int(cleaned_balance) + int(cleaned_amount_added)
#print("new_balance is : ", new_balance)
print(f"new_balnce is: {new_balance}")

sentence_3 = "CONFIRMED: you have recieved 40kes from Philip"
 
split_sentence_3 = sentence_3.split(" ")

print(f"the amount recieved is: {split_sentence_3[4]}")

balance = "12.02kes"
added_amount = "40kes"

cleaned_balance = balance.replace("kes", "")
print(f"cleaned balance is: {cleaned_balance}")
cleaned_added_amount = added_amount.replace("kes", "")
print(f"cleaned added amount is: {cleaned_added_amount}")

new_balance = float(cleaned_balance) + int(cleaned_added_amount)
print(f"new balance is: {new_balance}")





