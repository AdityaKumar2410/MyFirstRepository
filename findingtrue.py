# count in python to check the occurence of words or letters without spaces to count together
# lower function is used to convert all text to lowercase
print("The Love Calculator is calculating your score...")
name1 = input("Enter your name : \n") # What is your name?
name2 = input("Enter their name : \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

total_name_TRUE = name1 + name2
# to remove spaces we can use replace or join and split function.
# print(total_name_TRUE)

T = total_name_TRUE.count("t")
R = total_name_TRUE.count("r")
U = total_name_TRUE.count("u")
E = total_name_TRUE.count("e")
# print(T+R+U+E)
TRUE = str(T+R+U+E)

L=total_name_TRUE.count("l")
O=total_name_TRUE.count("o")
V=total_name_TRUE.count("v")
E = total_name_TRUE.count("e")
# score = (T+R+U+E) + (L+O+V+E)

lov= str(L+O+V+E)
score = TRUE + lov
score2 = int(score)
# print(TRUE+love)
if score2 < 10 or score2>90:
    print(f"Your score is {score2}, you go together like coke and mentos.")
elif score2 > 40 and score2<50:
    print(f"Your score is {score2}, you are alright together.")
else:
    print(f"Your score is {score2}.")
