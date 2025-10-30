from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for cb in checkboxes:
    if not cb.is_selected():
        cb.click()
        print("Clicked a checkbox...")
        time.sleep(1)  
    print("Checked:", cb.is_selected())
time.sleep(3)
driver.quit()