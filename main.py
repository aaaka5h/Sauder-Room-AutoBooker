import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from user_info import getUBCCredentials, getNumRepeatBookings, getBookings
# Sauder undergraduate room website
url = "https://booking.sauder.ubc.ca/ugr"

# UBC Credentials
username, password = getUBCCredentials()
repeat_bookings = getNumRepeatBookings()

# Bookings is (time, hours) tuples for each day of the week, repeat_bookings times
# e.g.
# bookings =  [
#   [("7:00", 1), ("8:00", 1), ("9:00", 2)], 
#   [("7:00", 1), ("8:00", 1), ("9:00", 2)]
#   ...]
bookings = getBookings(repeat_bookings)

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
cell_list_per_row = [row.find_elements(by=By.CSS_SELECTOR, value="td") for row in rows]
for cells in cell_list_per_row:
    for cell in cells:
        if not cell or cell.text == None: continue
        print("className", cell.get_property("className")) # booking status here

best_free_room = None
rows.reverse() # best rooms are last so move backwards

print(best_free_room)

time.sleep(50)
