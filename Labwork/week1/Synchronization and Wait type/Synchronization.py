
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.maximize_window()

try:
    # 1. Implicit Wait Demo
    driver.implicitly_wait(10)
    driver.get("https://testautomationpractice.blogspot.com/")
    name_field = driver.find_element(By.ID, "name")

    # 2. Explicit Wait Demo
    wait = WebDriverWait(driver, 10)
    point_me_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Point Me')]"))
    )
finally:
    driver.quit()