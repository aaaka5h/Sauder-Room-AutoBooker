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
def getNumRepeatBookings():
    repeat_bookings = 1
    while True:
        repeat_bookings = input("How many weeks would you like to book for (1 or 2)?\n")
        if repeat_bookings and repeat_bookings in ["1", "2"]:
            break
        print("Erorr: Please enter a valid number of weeks to book for\n")
    return int(repeat_bookings)

# Specify the time and duration of each booking
def getBookings(repeat_bookings):
    bookings = [[("FILL", 0) for _ in range(7)] for _ in range(repeat_bookings)]
    for i in range(0,repeat_bookings):
        print(f"Week {i+1}:")
        for j, day in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
            booking_info = input(f"Enter the time (24h format) and duration of your booking for {day} in the form HH:MM H.H (e.g: 7:00 1.5): ")
            if not booking_info: continue
            time, duration = booking_info.split(" ")
            bookings[i][j] = (time, float(duration))
    return bookings