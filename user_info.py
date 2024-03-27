import getpass

# UBC Credentials
def getUBCCredentials():
    while True:
        username = input("Please enter your CWL username\n")
        password = getpass.getpass("Please enter your CWL password\n")
        if username and len(username) and password and len(password):
            break
        print("Error: Your username or password is invalid\n")
    return username, password
    
# Number of weeks to repeat bookings for
def getRepeatBookings():
    repeat_bookings = 1
    while True:
        repeat_bookings = input("How many weeks would you like to book for?\n")
        if repeat_bookings and repeat_bookings.isdigit():
            break
        print("Erorr: Please enter a valid number of weeks to book for\n")
    return int(repeat_bookings)