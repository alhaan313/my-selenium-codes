# Whatsapp mass message sending
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time    

driver = webdriver.Edge()
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,100)
time.sleep(10)

target = '"Group 1 IBM"'
##message = "This message has been automated at {current_time} on {current_day}"
contact_path='//span[contains(@title,'+ target +')]'
contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()

#Group info click
group_info = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/header/div[2]/div[1]/div/span')
group_info.click()
time.sleep



message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))


message_box.send_keys(message + Keys.ENTER)
print(f"Message sent at {current_time} on {current_day}")
time.sleep(10)
driver.quit()
send_message()
