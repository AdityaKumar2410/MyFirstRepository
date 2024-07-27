#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# for n in range is used to run the loop as many times required as per the values assigned in range function
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_1 = ""
for char in range(0,nr_letters):
    # just to clarify here we have first used 1 and then nr_letters+1 because 1 to that no of times as per given by users . We can also do by writing 0 first but we will not write +1 at the end of nr_letters
    password_1 += random.choice(letters)
for num in range(0,nr_numbers):
    password_1 += random.choice(numbers)
for sym in range(0,nr_symbols):
    password_1+= random.choice(symbols)
password = list(password_1)
random.shuffle(password)
# here shuffle functionn does not return a new list but actually shuffles the original list so we need to print actually the same list
password_2 = "".join(password)
print(f"Your password is {password_2}")