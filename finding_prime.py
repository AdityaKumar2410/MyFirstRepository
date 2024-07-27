# Write your code below this line 👇
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            # prime = False
            break
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number

prime_checker(number=n)
# second way of doing the same thing
def prime_checker_2(num):
    is_prime = True#the problem here occuring was that we cannot change a global variable in a local area so if we want to change the variable inside a fuction we have to define it inside a function

    for i in  range(2, num):
        if num%i == 0:
            is_prime=False
    if is_prime==True:

        print("It is prime number!")
    else:
        print("It is not a prime number!!")
prime_checker_2(num = n)
