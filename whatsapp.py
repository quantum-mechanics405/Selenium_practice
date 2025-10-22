from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for manual login (scan the QR code)
print("Please scan the QR code for WhatsApp Web login.")
time.sleep(25)


# Locate the search bar where you can input the contact name
search_bar = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')

# Clear the search bar (optional, in case there's any pre-filled text)
search_bar.clear()

# Enter the search term "Maham"
search_bar.send_keys("Maham")

# Wait a bit to see the results appear
time.sleep(5)  # Adjust as needed

# Optionally press Enter to select the first result (if needed)
search_bar.send_keys(Keys.RETURN)

# Wait to see the chat open (you can remove or adjust this wait time)
time.sleep(8)


# Close the browser (optional)
# driver.quit()


print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')

print('Hello world')
