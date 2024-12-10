from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with your Instagram username and password
username = ""
password = ""

# Create a Chrome WebDriver object
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open Instagram
driver.get("https://www.instagram.com")

# Find the username and password fields and enter your credentials
username_type = driver.find_element(By.XPATH, '//input[@name="username"]')
username_type.send_keys(username)
password_type = driver.find_element(By.XPATH, '//input[@name="password"]')
password_type.send_keys(password)

# Submit the login form
password_type.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to the following page
driver.get("https://www.instagram.com/{}/following/".format(username))
time.sleep(2)

# Scroll to the bottom of the page to load all users
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find the buttons to unfollow
buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'x9f619')]")

# Iterate through the buttons and unfollow
for button in buttons:
    button.click()
    time.sleep(2)  # Add a delay between unfollow actions

    # Find the confirmation dialog
    confirm_dialog = driver.find_element(By.XPATH, '//div[@role="dialog"]')

    # Click the "Unfollow" button
    unfollow_button = confirm_dialog.find_element(By.XPATH, './/button[text()="Unfollow"]')
    unfollow_button.click()

    # Scroll to the next button
    driver.execute_script("arguments[0].scrollIntoView();", button)
    time.sleep(2)

# Close the browser
