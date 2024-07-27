# import random
# from data_higherlowergame import data
# from higher_lower_game_ascii_art import ascii_art
# points = 0
# last_choice_B = None
# while True:
#     print(f"Points={points}")
#     choice_random_first = random.choice(data)
#     # print(choice_random["follower_count"])
#     choice_random_second = random.choice(data)
#     if points >=1:
#         choice_random_second = last_choice_B
#     name_first=choice_random_first["name"]
#     name_second=choice_random_second["name"]
#     description_first=choice_random_first["description"]
#     description_second=choice_random_second["description"]
#     country_first=choice_random_first["country"]
#     country_second=choice_random_second["country"]
#     folower_count_first = choice_random_first["follower_count"]
#     folower_count_second = choice_random_second["follower_count"]
#     print(f"Compare A: {name_first} a {description_first} from {country_first}.")
#     print(ascii_art)
#     print(f"Compare B: {name_second} a {description_second} from {country_second}.")
#     print(f"A: {choice_random_first['follower_count']}, B: {choice_random_second['follower_count']}")
#     user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
#     def more():
#         if choice_random_first["follower_count"] > choice_random_second["follower_count"]:
#             return "A"
#         else:
#             return "B"
#
#
#
#     result = more()
#     if user_choice == result:
#
#         points += 1
#         print("You Win!")
#         if result=="A":
#             last_choice_B = choice_random_first
#         else:
#             last_choice_B = choice_random_second
#
#
#     else:
#         print("You lose!")
#         break

# here is a way better to do this



import random
from data_higherlowergame import data
from higher_lower_game_ascii_art import ascii_art
points = 0
last_choice_B = None

def unique_choice(exclude_choice):
    choice=random.choice(data)
    while choice == exclude_choice:
        choice=random.choice(data)
    return choice
def info(choice_a,choice_b):
    print(f"Compare A: {choice_a['name']} a {choice_a['description']} from {choice_a['country']}.")
    print(ascii_art)
    print(f"Compare B: {choice_b['name']} a {choice_b['description']} from {choice_b['country']}.")
    print(f"A: {choice_a['follower_count']}, B: {choice_b['follower_count']}")
def more_followers_count(choice_a,choice_b):
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return 'A'
    else:
        return 'B'
while True:
    choice_a = random.choice(data)
    choice_b = unique_choice(choice_a)

    if points>=1 and last_choice_B:
        choice_b = last_choice_B
    info(choice_a,choice_b)
    user_guess = input("Guess who has more followers: ").upper()
    result = more_followers_count(choice_a,choice_b)

    if user_guess==result:
        print("You Win!!!")
        points+=1

        if user_guess == "A":
            last_choice_B = choice_a
        else:
            last_choice_B = choice_b
    else:
        print("You Lose!!!!")
        break










