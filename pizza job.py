print("Thank you for choosing Python Pizza Deliveries!")

# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1

size = input("Enter the size of pizza you want . Enter'L' for large-sized,'M' for medium size and 'S'for small-sized pizza ")  # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepporoni or not. Enter'Y' for yes and 'N' for no")  # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheeese? Y or N")  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "l" or "L":
    print("You have selected a large-sized pizza and that would cost you a hopping 25$")
    bill = 25
elif size=="m" or"M":
    print("You have selected a medium-sized pizza and that would cost you a hopping 20$")
    bill = 20
elif size == "s" or"s":
    print("You have selected a small-sized pizza and that would cost you a hopping 15$")
    bill = 15
else:
    print("Give input as per the instructions given above")
if add_pepperoni=="Y":
    if size == "L" or size=="l":
        print("Extra pepporoni would add a hopping 3$ on your bill")
        bill += 3
    elif size =="M" or size =="m":
        print("Extra pepporoni would add a hopping 3$ on your bill")
        bill += 3
    else:
        print("Extra pepporoni would add a hopping 2$ on your bill ")
        bill +=2
else:
    print("You have not selected adding pepporoni ")
if extra_cheese == "Y":
    print("You have selected for adding extra cheese. That would add 1$ on your bill.")
    bill += 1
elif extra_cheese == "N":
    print("You have not selected for adding extra cheese. ")
else:
    print("Enter as per the instructions given above.")
print(f"Your total bill is {bill}")
print("Thank you , for selecting python pizza as your choice.")
