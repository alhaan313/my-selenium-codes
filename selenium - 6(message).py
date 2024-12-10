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
not_now = driver.find_element(By.XPATH, "//button[text()='Not Now']")
not_now.click()

search = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div")
search.click()

search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_input.send_keys("alhaan313" + Keys.ENTER)
