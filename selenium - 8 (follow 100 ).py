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


#Navigate to your profile page
driver.get("https://www.instagram.com/fiberestar/followers/")
# Wait for the page to load
time.sleep(2)

flp = driver.find_element(By.CLASS_NAME, "_aano")
buttons = flp.find_elements(By.TAG_NAME, "button")
i = 0
follow_text = driver.find_elements(By.CLASS_NAME, "_aacl _aaco _aacw _aad6 _aade")

# Find the container element of the new box
box_container = driver.find_element(By.CLASS_NAME, "_aano")
driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", box_container)

while (i<100):
##    for i in follow_text:
##        print(i.text)
    for button in buttons:
        inner_html = button.get_attribute("innerHTML")
        if "Follow" in inner_html and "Following" not in inner_html:
            button.click()
            time.sleep(1)  # Wait for
            i+=1
