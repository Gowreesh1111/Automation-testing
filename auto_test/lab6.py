from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# ✅ Correct locator for the Login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for the message to appear
time.sleep(2)

# Capture and print the message
message = driver.find_element(By.ID, "flash").text
print("Message:", message)

# Close browser
driver.quit()
