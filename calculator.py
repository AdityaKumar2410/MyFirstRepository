# # this is a program to create a calculator for the program to work
#
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """
#
# def clean():
#     print("\n"*100)
#
#
# def add(first,second):
#     return first+second
# def subtract(first,second):
#     return first-second
# def multiply(first,second):
#     return first*second
# def divide(first,second):
#     return first/second
#
# operations = {
#     "*":multiply,
#     "+":add,
#     "-":subtract,
#     "/":divide
# }
#
# answer = 0
# def calculations():
#     print(logo+"\n")
#     num1 = float(input("Enter the first number: "))
#     for symbol in operations:
#         print(symbol)
#     # second_number = int(input("Enter the second number: "))
#     while True:
#         choice = input("Enter your choice for performing calculation: ")
#         value = operations[choice]
#         num2 = float(input("Enter the second number:"))
#         clean()
#         answer = value(num1, num2)
#         print(f"{num1}{choice}{num2}={answer}")
#         more_cal = input("If you want to continue with the same value then enter 'y' or if you want to start a new calculation then enter 'n' otherwise enter 'exit' for exiting the program!")
#         if more_cal == 'y':
#             num1 = answer
#         elif more_cal == 'n':
#             clean()
#             calculations()
#         else:
#             break
# calculations()
#
#

i =0
while 500000000000000000000000000000000000>i:
    result = i+i
    print(result)
    if i == 0:
        i+=1

        continue
    i = result