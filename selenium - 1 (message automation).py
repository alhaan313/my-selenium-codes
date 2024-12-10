#WHATSAPP MESSAGE AUTOMATION

import schedule
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
##from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def send_message():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_day = datetime.now().strftime("%A")
    if current_day == "Sunday":
        print("Today is Sunday, skipping message send...")
        return
    
##    options = webdriver.ChromeOptions()
    driver = webdriver.Edge()
    driver.get("https://web.whatsapp.com/")
    wait=WebDriverWait(driver,100)
    time.sleep(25)

    target = '"Mother"'
    message = "This message has been automated at {current_time} on {current_day}"
    contact_path='//span[contains(@title,'+ target +')]'
    contact=wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
    contact.click()
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))

    
    message_box.send_keys(message + Keys.ENTER)
    print(f"Message sent at {current_time} on {current_day}")
    time.sleep(10)
    driver.quit()
send_message()















##
##schedule.every().day.at("23:49").do(send_message)
##
##
##
##while True:
##    schedule.run_pending()
##    time.sleep(1)
