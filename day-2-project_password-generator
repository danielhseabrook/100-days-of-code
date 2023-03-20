#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

for n in range(0,nr_letters):
  random_letter = random.randint(0,49)
  password += letters[random_letter]

for n in range (0,nr_numbers):
  random_number = random.randint(0,9)
  password += numbers[random_number]

for n in range (0,nr_symbols):
  random_symbol = random.randint(0,8)
  password += symbols[random_symbol]

#splitting to the password into a list
password_split = list(password) 
#shuffling the list
random.shuffle(password_split)
#rejoining the list into a string
password = "".join(password_split)
print(password)
