import random
import string

# Create a list of available letters, numbers and symbols
letters = list(string.ascii_lowercase)
upper_case_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list('!#$%&()*+')


# Choose the characters to be included in the password
password_list = []
for _ in range(4):
    password_list.append(random.choice(letters))
    password_list.append(random.choice(numbers))
    password_list.append(random.choice(symbols))
    password_list.append(random.choice(upper_case_letters))

# Scramble the characters selected and concatenate them into a string of 15 digits
random.shuffle(password_list)
password = ''.join(password_list[:15:])

# Present the password to the user
print("Password generated:")
print(password)
