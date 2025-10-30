from selenium import webdriver
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)

# Take a screenshot
driver.save_screenshot("google.png")
print("Screenshot saved!")

# Close the browser
driver.quit()
