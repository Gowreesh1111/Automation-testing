from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open the website
driver.get("https://the-internet.herokuapp.com/dropdown")

# Wait a bit to ensure the page loads
time.sleep(10)

# Locate the dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown"))

# Select Option 2
dropdown.select_by_visible_text("Option 2")

# Print the selected option
print("Selected:", dropdown.first_selected_option.text)

# Close the browser
driver.quit()

