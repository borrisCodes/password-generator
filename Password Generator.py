#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

while nr_letters > 0:
  letter_selection = random.randint(0, len(letters) - 1)
  password += letters[letter_selection]
  nr_letters -= 1

while nr_numbers > 0:
  number_selection = random.randint(0, len(numbers) - 1)
  password += numbers[number_selection]
  nr_numbers -= 1

while nr_symbols > 0:
  symbol_selection = random.randint(0, len(symbols) - 1)
  password += symbols[symbol_selection]
  nr_symbols -= 1

password_var = list(password)

random.shuffle(password_var)

print (''.join(password_var)) 