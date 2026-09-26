import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    print("--- 1. Opening Login Page ---")
    driver.get("https://practice.softwaretestingmentor.com/login")
    time.sleep(2)

    # TRY BLOCK: Attempt to locate non-existent element
    driver.find_element(By.ID, "invalid_fake_id").click()

except NoSuchElementException:
    # EXCEPT BLOCK: Catches NoSuchElementException cleanly
    print("[HANDLED] Caught NoSuchElementException! Element not found on page.")

finally:
    # FINALLY BLOCK: Always executes browser cleanup
    time.sleep(2)
    driver.quit()
    print("[FINALLY] Browser closed safely.")