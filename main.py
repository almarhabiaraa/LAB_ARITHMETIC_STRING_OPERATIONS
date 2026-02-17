# Python program to calculate the total cost of a customer's purchase, including tax.

# First Attempt (With Errors):

'''
price = 2.99
quantity = 3
tax_rate = 7.5
subtotal = (price * quantity)

tax = (subtotal * tax_rate)
total_cost =(subtotal + tax)


print("Price of item:" + "$" + (round(price, 2)))
print("Quantity:" + quantity)
print("Tax rate:" + (round(tax_rate, 2)) + "%")


print()
print("Subtotal:" + "$" + (round(subtotal, 2)))
print("Tax:" + "$" + (round(tax, 2)))
print("Total:" + "$" + (round(total_cost, 2)))

'''

'''
My first attempt at solving the problem was written as follows.
While working on it, I encountered some errors related to calculations and data formatting. I reviewed the mistakes and searched for solutions, which helped me understand the correct approach. 
After fixing the issues, I reached the corrected version shown below.

'''

# Corrected Version:



price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")

print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")



# Bouns -  create a new python file and do the following:

# Define a string variables
about_me:str = "Hello, my name is Araa Almarhabi, I am studying web development using Python at Tuwaiq Academy"

programming_language:str = "Python" 

# Length 
print(len(about_me))
print(len(programming_language))


# Print the index of the first occurrence of the word in the sentence.
print(programming_language[0])

# Print the number of times the word appears in the sentence.
print(about_me.count(programming_language))

# Print the sentence in all uppercase letters.
print(about_me.upper())

# Print the sentence in all lowercase letter. 
print(about_me.lower())
# Replace the word in the sentence with a new word of your choice.
print(about_me.replace("Python", "Java"))

# Print the last character of the sentence.
print(about_me[-1])


