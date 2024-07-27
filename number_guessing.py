# this is a program to create a numberguessing program
import random
computer_choice = random.randint(0,101)
print(computer_choice)
lives = 0

def level():
    global lives
    easy_difficulty = input("Enter the difficulty level to start!Enter 'e' for easy and 'h' for hard\n").lower()
    if easy_difficulty=="e":
        lives = 10
    elif easy_difficulty=="h":
        lives = 5
    else:
        print("Enter as per the instructions only!!")

def main():
    level()
    global lives
    while True :

        user_choice = int(input("Enter your choice of numberguessed between 1 and 100:  "))
        if user_choice == computer_choice:
            print("You win!!!")
            break
        else:
            print("Oh!That was a wrong choice!make sure you make choices accurately!otherwise you are going to lose lives!")
            if user_choice>computer_choice:
                print("High")
            elif user_choice<computer_choice:
                print("Low")
            lives-=1
        if lives == 0:
            print("You lost the game!!!")
            break

main()
more_game = input("If you want to continue then enter 'y' otherwise enter 'n': ")
if more_game == 'y':
    main()
else:
    print("Thank you for playing the game!!!")
