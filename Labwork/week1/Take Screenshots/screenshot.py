# =========================================================================
# TAKE SCREENSHOTS AND GENERIC METHOD TO TAKE SCREENSHOTS
# Website: https://practice.softwaretestingmentor.com/login
# Demonstrates 2 pictures:
# 1. Direct Method (Before credentials)
# 2. Generic Method (After entering Name & Password)
# =========================================================================

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options to handle Cloudflare verification
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# =========================================================================
# GENERIC METHOD TO TAKE SCREENSHOT
# =========================================================================
def take_screenshot(driver, file_name):
    """Generic reusable function to capture and save screenshot in current directory."""
    driver.save_screenshot(file_name)
    print(f"[GENERIC METHOD] Screenshot saved successfully -> {file_name}")

try:
    # 1. Open login page
    driver.get("https://practice.softwaretestingmentor.com/login")
    time.sleep(3)

    # 2. Picture 1: DIRECT METHOD (Before entering credentials)
    driver.save_screenshot("before_credentials.png")
    print("[DIRECT METHOD] Screenshot saved -> before_credentials.png")

    # 3. Enter Username and Password
    user_input = driver.find_element(By.ID, "username")
    user_input.clear()
    user_input.send_keys("DemoUser")

    pass_input = driver.find_element(By.ID, "password")
    pass_input.clear()
    pass_input.send_keys("DemoPassword123")
    time.sleep(1)

    # 4. Picture 2: GENERIC METHOD (After entering name & password)
    take_screenshot(driver, "after_credentials.png")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser closed successfully.")