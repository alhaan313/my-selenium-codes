from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a Chrome WebDriver object
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open Instagram
driver.get("https://inflact.com/tools/instagram-search/")
# Wait for the page to load
time.sleep(2)

country = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[3]/div/div[2]/div[2]")
country.click()

country_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[3]/div/div[4]/div[1]/input")
country_search.click()

country_search.send_keys("India")
India = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[3]/div/div[4]/div[2]/div[89]")
India.click()

gender = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[6]/div/div[2]/div[2]")
gender.click()
male = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[6]/div/div[4]/div/div[2]")
male.click()

category = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[7]/div/div[2]/div[2]")
category.click()
category_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[7]/div/div[4]/div[1]/input")
category_input.click()
category_input.send_keys("Advertising/Marketing")

advertising = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[4]/div[2]/div[7]/div/div[4]/div[2]/div[47]")
advertising.click()

update = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form[1]/div[2]/button")
update.click()

#FILTERS DONE
time.sleep(10)
ig_result = driver.find_elements(By.CLASS_NAME, "result-info")
ig_1 = []
ig_2 = []
for i in ig_result:
    a = i.find_element(By.TAG_NAME, 'a')
    print(a.text)
##    ig_1.append(a.text)
##for text in ig_1:
##    print(text)
##ig_1 = ig_result.find_elements(By.TAG_NAME, 'a')
##ig_2 = ig_result.find_elements(By.CLASS_NAME, 'info-title')
##
##for i in ig_1.text:
##    print(i)
    
