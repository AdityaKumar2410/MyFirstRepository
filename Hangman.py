import random
from hangman_wordlist import word_list
from hangman_asciii_art import stages
from hangman_asciii_art import logo

print(logo)

lives = 6
points = 0

computer_choice_random = random.choice(word_list)
print(computer_choice_random)

blank_computer = []

for _ in range(len(computer_choice_random)):
    blank_computer+="_"

print(''.join(blank_computer))
game_start = True
while game_start == True:
    if "_" not in blank_computer:
        computer_choice_random = random.choice(word_list)
        print(computer_choice_random)
        blank_computer = []
        lives = 0
        for _ in range(len(computer_choice_random)):
            blank_computer += "_"
    print(stages[lives])
    user_input = input("Enter your choice of letter as per the word you have guesses: \n").lower()

    if user_input=="exit":
        print("You have chosen to exit!!\nThankyou for using this program!!")
        break
    if user_input in blank_computer:
        print("It has been alredy repeated!")
        continue
        # here continue word repeats the loop from start
    for position in range(len(computer_choice_random)):
        # we dont need here to convert the string computer choice random to list because if will run here the interepreter will automatically check for the letters here in the word of computer_choice_random
        letter = computer_choice_random[position]
        if letter == user_input:
            blank_computer[position] = letter
            # print(stages)

    if user_input not in computer_choice_random or user_input.strip()=="" :
        if user_input.strip() =="":
            print("Enter as per the instructions only!! By this way you are going to lose lives!!!!")
        lives-=1


        if lives==0:
            print("We are starting the from beginning .If you want to exit just enter'exit' or if you want to continue enter 'continue' ")
            end_continue = input("Enter exit or continue!")
            points -=1
            if end_continue == "exit":
                break
            elif end_continue == "continue":
                print("You have chosen to restart the game.")
                continue

    print(stages[lives])
            # print(stages[lives])
    # print(f"You are on {lives} stage. ")

    # this is one way to do this another way is this


    # for letter in computer_choice_random:
    #     if letter == user_input:
    #         letter_position = computer_choice_random.index(user_input)
    #         # print(letter_position)
    #         blank_computer[letter_position] = user_input
    #     # this is more clearer way for me as first we go through all the letters in the word of computer_choice_random and then find the index of letter in the word of computer_choice_randon
    #     # here the index function will not work as desired because the index function returns only the first time the elment occurs in the list

    print(''.join(blank_computer))
    if "_" not in blank_computer:
        end_continue = input("Enter exit or continue!")
        points += 1
        if end_continue == "exit":
            break
        elif end_continue == "continue":
            print("You have chosen to restart the game.")
            continue
        print("You guessed all the letters!!!!!")
        print("We have increased your points by 1! If you want to exit you can enter'exit'!")
        points +=1
        continue
# one more extinction i am adding is to continue the game until the user chooses to exit
