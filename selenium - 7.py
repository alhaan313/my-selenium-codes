 #UNFOLLOW EVERYONE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a Chrome WebDriver object
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

# Open Youtube
driver.get("https://www.youtube.com")
4

# Find Content

content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contents")))
travContent = driver.find_elements(By.CLASS_NAME,'style-scope ytd-rich-grid-media')
for var in travContent:
    var.find_element(By.TAG_NAME, 'yt-formatted-string')
    print(var.text)                                        
