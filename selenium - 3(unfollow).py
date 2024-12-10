#UNFOLLOW EVERYONE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your Instagram username and password
username = ""
password = ""

# Create a Chrome WebDriver object
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open Instagram
driver.get("https://www.instagram.com")

# Wait for the page to load
time.sleep(2)

# Find the username and password fields and enter your credentials
username_type = driver.find_element("xpath",'//input[@name=\"username\"]')
username_type.send_keys(username)
password_type = driver.find_element("xpath",'//input[@name=\"password\"]')
password_type.send_keys(password)

# Submit the login form
password_type.send_keys(Keys.RETURN)

# Wait for the page to load after login
time.sleep(5)

# Navigate to your profile page
driver.get("https://www.instagram.com/{}".format(username))

# Wait for the page to load
time.sleep(2)

# Click on the followers link
followers_link = driver.find_element(By.XPATH, '//a[@href="/{}/following/"]'.format(username))
followers_link.click()

# Wait for the followers page to load
time.sleep(5)

# Find the container element of the new box
box_container = driver.find_element(By.CLASS_NAME, "_aano")

# Scroll within the new box
last_box_height = driver.execute_script("return arguments[0].scrollHeight", box_container)
while True:
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", box_container)
    time.sleep(5)
    new_box_height = driver.execute_script("return arguments[0].scrollHeight", box_container)
    if new_box_height == last_box_height:
        break
    last_box_height = new_box_height

flp = driver.find_element(By.CLASS_NAME, "_aano")
buttons = flp.find_elements(By.TAG_NAME, "button")
b4 = driver.find_elements("xpath", "//button[contains(@class, 'x9f619')]")

for button in buttons:
    button.click()
    confirm_dialog = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div')

    # Click the "Unfollow" button
    unfollow_button = confirm_dialog.find_element(By.XPATH, './button[1]')
    unfollow_button.click()
