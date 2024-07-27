import random

print("Welcome to The Game of Rock Paper Scissor..... ")

# ASCII Art for the game choices
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# List of images to display based on user or computer choice
images = [rock, paper, scissors]

# Function to get the user's choice
def get_user_choice():
    while True:
        user_input = int(input("Enter your choice... 0 for rock, 1 for paper, and 2 for scissors: "))
        if 0 <= user_input <= 2:
            return user_input
        else:
            print("Invalid input. Please enter 0, 1, or 2.")

# Get the user's and computer's choices
user_choice = get_user_choice()
computer_choice = random.randint(0, 2)

# Display the choices
print(f"You chose:\n{images[user_choice]}")
print(f"Computer chose:\n{images[computer_choice]}")

# Determine the winner
if user_choice == computer_choice:
    print("This is a tie!!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You won!!!")
else:
    print("Computer won!!! Better luck next time!")

print("Thank you for using this program!")
