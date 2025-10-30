from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find search box and search for "Python Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Get top 5 results
results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

# Print each result title
for r in results:
    print(r.text)

# Close browser
driver.quit()
