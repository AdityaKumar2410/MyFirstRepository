records = {}
print("Welcome to secret bidding!!!")
print("You firt have to entr name and then your bid!!")
def clear_screen():
    print("\n"*100)

def add():
    name = input("Enter your name: \n")
    bid = int(input("Enter the amount: $"))

    records[name] = bid
def max_bid():
    highest_bid = 0
    for names,value in list_records:#records.items returns a list consisting if tupils with first element of tupil as the key and the 2nd element as value
        if value>highest_bid:
            highest_bid = value
            winner = names
    return f"The winner is {winner}"

def more_bid():
    while True:
        more_bidders = input("If there ae more bidders enter'y' otherwise enter 'n'.\n ").lower()

        if more_bidders == 'y':
            clear_screen()
            add()
        elif more_bidders == 'n':
            clear_screen()
            break
        else:
            print("Enter as per the instructions.!!!!!!!!!~!")
            more_bid()

list_records = records.items()

add()
more_bid()

print(max_bid())
