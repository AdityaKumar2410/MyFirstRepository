line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter where you want to mark the X").lower() # Where do you want to put the treasure?
position_letter = position[0]
position_no = int(position[1])-1
abc = ["a","b","c"]
position_letter_no = abc.index(position_letter)
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# # position_element = position[0].lower()
# element_no = ["a","b","c"]
# position_element_no = element_no.index(position_element)
# position_row_no = int(position[1])-1
# map[position_row_no][position_element_no] = "X"
# here we have used first because position row no is the the first letter because the index is like :
#     # here the letter is the element no so we created here a list to get the row no so we could also use conditions as per the need
#     A B C
# 1= [0,1,2]
# 2 = [0,1,2]
# 3 = [0,1,2]


# Write your code above this row 👆
# 🚨 Don't change the code below 👇

# there is also one more way to do this
# we can use conditions here
if position_no == 0:
    map[0][position_letter_no] = "X"
elif position_no == 1:
    map[1][position_letter_no] = "X"
elif position_no == 2:
    map[2][position_letter_no] = "X"
else:
    print("Enter a valid index")
print(f"{line1}\n{line2}\n{line3}")
# this is one more way to do this