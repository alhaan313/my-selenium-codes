#WHATSAPP AUTOMATION
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome WebDriver options to run headless and in incognito mode
chrome_options = OptSions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-dev-shm-usage')


# Open a new instance of the Chrome WebDriver and go to the WhatsApp web URL
driver = webdriver.Chrome(executable_path='D:\Selenium Chrome Driver', options=chrome_options)
driver.get('https://web.whatsapp.com')


# Wait for user to scan QR code and log in manually
input('Scan the QR code and press any key to continue...')

# Define a function to send a message to a selected contact or group
def send_message():
    # Replace 'contact_name_or_group_name' with the name of the contact or group you want to send the message to
    contact_name_or_group_name = 'muzaina'

    # Replace 'your_message_here' with the message you want to send
    message = 'ASSalamualaikum'

    # Find and click on the contact or group
    contact_or_group = driver.find_element_by_xpath("//span[@title='"+contact_name_or_group_name+"']")
    contact_or_group.click()

    # Find and click on the message input field
    message_input = driver.find_element_by_xpath("//div[@contenteditable='true']")
    message_input.click()

    # Enter the message and send it
    message_input.send_keys(message)
    message_input.submit()

# Call the send_message() function
send_message()

# Close the browser window
driver.quit()
