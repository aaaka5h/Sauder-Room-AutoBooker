import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from secret import USERNAME, PASSWORD

# Sauder undergraduate room website
url = "https://booking.sauder.ubc.ca/ugr"

# UBC Credentials
username = USERNAME
password = PASSWORD

driver = webdriver.Chrome()

driver.get(url)

# Sleep for 5
time.sleep(1)

title = driver.title

driver.implicitly_wait(0.5)

# Authenticate with UBC CWL
cwl_login = driver.find_element(by=By.CLASS_NAME, value="logon")
cwl_login_button = cwl_login.find_element(by=By.CSS_SELECTOR, value='input[type="submit"][value="CWL Login"]')

cwl_login_button.click()
time.sleep(0.5)

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

# So far so good


    
