sentence = "you have recieved 40kes from Philip"

split_sentence = sentence.split(" ")

print(f"the amount recieved is: {split_sentence[3]}")

balance = "12.02kes"
added_amount = "40kes"

cleaned_balance = balance.replace("kes", "")
print(f"cleaned_balance is: {cleaned_balance}")

cleaned_added_amount = added_amount.replace("kes", "")
print(f"cleaned_added_amount is :{cleaned_added_amount}")

new_balance = float(cleaned_balance) + int(cleaned_added_amount)
print(f"new balance is: {new_balance}")

