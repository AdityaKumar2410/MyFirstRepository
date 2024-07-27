# print("hello world").jus
print("Welcome to circus Roller coaster")
height=int(input("Enter your height in cm after measuring it from the counter.Write the true height only as you will be checked by the machines then: \n"))

if height >=120:
    print("You are eligible but first tell your age")
    age =float(input("Enter your age: \n"))
    if age <= 12:
        print("We would charge you 5$")
        bill = 5
    elif age<=30:
        print("We would charge you 8$")
        bill = 8
    elif age<=60:
        print("We would charge you 10$")
        bill = 10

    else:
        print("Your age does not allow us to let you continue on the ride")
        bill = 0
    if age <= 60:
        camera_permission = input("Do you want your photo while riding the roller coaster? 'y' for yes and 'N' for no?And that would cost you extra 3$ on your bill")
        if camera_permission=="Y" or camera_permission=="y":
            bill+=3
            print(f"You can continue and the ride would cost you a hopping {bill}$")
        else:
            print(f"Your bill would be {bill}$")
    else:
        print("Sorry and we request you to suggest to your relatives who are below 60 years")
else:
    print("You have to grow taller before you continue on this ride.\n")
    print("Thank you")
