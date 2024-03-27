import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from user_info import getUBCCredentials, getRepeatBookings
# Sauder undergraduate room website
url = "https://booking.sauder.ubc.ca/ugr"

# UBC Credentials
username, password = getUBCCredentials()
repeat_bookings = getRepeatBookings()

# Bookings is (time, hours) tuples for each day of the week, repeat_bookings times
# e.g.
# bookings =  [
#   [("7:00", 1), ("8:00", 1), ("9:00", 2)], 
#   [("7:00", 1), ("8:00", 1), ("9:00", 2)]
#   ...]
bookings = [[("FILL", 0) for i in range(7)] for j in range(repeat_bookings)]

# Selenium script starts
driver = webdriver.Chrome()
driver.get(url)
title = driver.title
driver.implicitly_wait(0.5)

# Authenticate with UBC CWL
cwl_login = driver.find_element(by=By.CLASS_NAME, value="logon")
cwl_login_button = cwl_login.find_element(by=By.CSS_SELECTOR, value='input[type="submit"][value="CWL Login"]')

cwl_login_button.click()

# Enter CWL credentials
username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(username)

password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(password)

login_button = driver.find_element(by=By.NAME, value="_eventId_proceed")
login_button.click()

# Wait while user manually does MFA
while True:
    try:
        driver.find_element(by=By.CLASS_NAME, value="mrbs")
    except Exception as e:
        continue
    else:
        break

tbody = driver.find_element(by=By.CSS_SELECTOR, value="tbody")
rows = tbody.find_elements(by=By.CSS_SELECTOR, value="tr") 

best_free_room = None
rows.reverse() # best rooms are last so move backwards
for row in rows:
    cells = row.find_elements(By.CSS_SELECTOR, value="td")
    for cell in cells:
        booking_status = cell.get_attribute("class")
        if booking_status == "new":
            best_free_room = cell
            break
    if not best_free_room:
        print("No free room found at requested time :(")
        break

print(best_free_room)

time.sleep(50)
