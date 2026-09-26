# =========================================================================
# PREVIOUS CODE (BLOGSPOT WEBSITE) - COMMENTED OUT
# =========================================================================
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    # 1. Handling Alert Box
    alert_btn = driver.find_element(By.ID, "alertBtn")
    alert_btn.click()
    alert = driver.switch_to.alert
    alert.accept()

    # 2. Handling Datepicker
    datepicker = driver.find_element(By.ID, "datepicker")
    datepicker.clear()
    datepicker.send_keys("01/01/2026")

    # 3. Handling File Upload
    file_input = driver.find_element(By.ID, "singleFileInput")

    # 4. Handling Multiple Windows / Tabs
    main_handle = driver.current_window_handle
    driver.find_element(By.ID, "PopUp").click()

    # 5. Working with Keyboard Events
    actions = ActionChains(driver)

    # 6. Working with Scrollbar
    driver.execute_script("window.scrollBy(0, 400);")

    # 7. Working with Drag and Drop
    source_elem = driver.find_element(By.ID, "draggable")
    target_elem = driver.find_element(By.ID, "droppable")

    # 8. Handling Iframes
    driver.switch_to.frame("frame-one743126208")

    # 9. Find The State Of A Web Element
    is_enabled = element.is_enabled()

    # 10. Get Text & Attribute Value
    text_val = element.text

finally:
    driver.quit()
"""


# =========================================================================
# NEW IMPLEMENTATION: PRACTICE SOFTWARE TESTING MENTOR
# Website: https://practice.softwaretestingmentor.com/
# Syllabus Topics Covered:
# 1. Handling Alert Box
# 2. Handling Datepicker
# 3. Handling File upload
# 4. Handling multiple windows/Tabs
# 5. Working with keyboard events
# 6. Working with scrollbar
# 7. Working with drag and drop
# 8. Handling Iframes
# 9. Find The State Of A Web Element (Disabled And Enabled)
# 10. Get The Text On Element, Get Value Of Element Attribute
# =========================================================================

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

def open_url(url):
    """Helper function to load URLs safely with retry logic."""
    for _ in range(3):
        try:
            driver.get(url)
            time.sleep(3)
            return
        except Exception:
            time.sleep(2)

try:
    # =========================================================================
    # 1. HANDLING ALERT BOX
    # =========================================================================
    print("\n--- 1. HANDLING ALERT BOX ---")
    open_url("https://practice.softwaretestingmentor.com/js-alert")

    # Click button to trigger JavaScript alert
    alert_btn = driver.find_element(By.ID, "trigger-alert-btn")
    alert_btn.click()
    time.sleep(1)

    # Switch to alert, get text, and accept it
    alert = driver.switch_to.alert
    print(f"Alert Box Text -> '{alert.text}'")
    alert.accept()
    print("Accepted Alert Box successfully!")
    time.sleep(1)

    # =========================================================================
    # 2. HANDLING DATEPICKER
    # =========================================================================
    print("\n--- 2. HANDLING DATEPICKER ---")
    open_url("https://practice.softwaretestingmentor.com/calendar")

    try:
        date_input = driver.find_element(By.XPATH, "//input[@type='date'] | //input[contains(@class,'date')] | //input")
        date_input.clear()
        date_input.send_keys("2026-01-01")
        print(f"Datepicker Selected Date -> '{date_input.get_attribute('value')}'")
    except Exception as e:
        print(f"Datepicker handling: {e}")
    time.sleep(1)

    # =========================================================================
    # 3. HANDLING FILE UPLOAD
    # =========================================================================
    print("\n--- 3. HANDLING FILE UPLOAD ---")
    open_url("https://practice.softwaretestingmentor.com/file-upload")

    # Create a temporary dummy file for upload demonstration
    dummy_file_path = os.path.abspath("demo_upload_sample.txt")
    with open(dummy_file_path, "w") as f:
        f.write("Selenium File Upload Test Content")

    # Send absolute path to the file input element
    file_input = driver.find_element(By.ID, "uploadFile")
    file_input.send_keys(dummy_file_path)
    print(f"Uploaded File Value -> '{file_input.get_attribute('value')}'")
    time.sleep(1)

    # Clean up local dummy file
    if os.path.exists(dummy_file_path):
        os.remove(dummy_file_path)

    # =========================================================================
    # 4. HANDLING MULTIPLE WINDOWS / TABS
    # =========================================================================
    print("\n--- 4. HANDLING MULTIPLE WINDOWS / TABS ---")
    open_url("https://practice.softwaretestingmentor.com/multiple-windows")

    main_window = driver.current_window_handle
    print(f"Main Window Handle -> {main_window}")

    # Click link configured with target='_blank' to open a new tab/window
    new_tab_link = driver.find_element(By.XPATH, "//a[@target='_blank']")
    new_tab_link.click()
    time.sleep(2)

    # Iterate through all open window handles
    all_handles = driver.window_handles
    print(f"Total Open Windows/Tabs -> {len(all_handles)}")

    for handle in all_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            print(f"Switched to New Window/Tab Title -> '{driver.title}'")
            time.sleep(1)
            driver.close()  # Close child tab

    # Switch back to the main window
    driver.switch_to.window(main_window)
    print("Switched back to Main Window.")
    time.sleep(1)

    # =========================================================================
    # 5. WORKING WITH KEYBOARD EVENTS
    # =========================================================================
    print("\n--- 5. WORKING WITH KEYBOARD EVENTS ---")
    open_url("https://practice.softwaretestingmentor.com/login")

    user_field = driver.find_element(By.ID, "username")
    user_field.clear()
    user_field.send_keys("KeyboardDemoUser")
    time.sleep(1)

    # Perform keyboard shortcut (CTRL + A -> BACKSPACE) using ActionChains
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
    time.sleep(1)

    # Type new value after clearing
    user_field.send_keys("UpdatedViaKeyboard")
    print(f"Input value after Keyboard Events -> '{user_field.get_attribute('value')}'")
    time.sleep(1)

    # =========================================================================
    # 6. WORKING WITH SCROLLBAR
    # =========================================================================
    print("\n--- 6. WORKING WITH SCROLLBAR ---")

    # Scroll down 300 pixels using JavaScript
    driver.execute_script("window.scrollBy(0, 300);")
    print("Scrolled down 300 pixels.")
    time.sleep(1)

    # Scroll element into center of viewport
    login_btn = driver.find_element(By.ID, "login-btn")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_btn)
    print("Scrolled Sign In button into view.")
    time.sleep(1)

    # =========================================================================
    # 7. WORKING WITH DRAG AND DROP
    # =========================================================================
    print("\n--- 7. WORKING WITH DRAG AND DROP ---")
    open_url("https://practice.softwaretestingmentor.com/drag-drop")

    try:
        source = driver.find_element(By.ID, "drag-item-1")
        target = driver.find_element(By.ID, "drag-target-box")
        ActionChains(driver).drag_and_drop(source, target).perform()
        print("Performed Drag and Drop using ActionChains!")
    except Exception as e:
        print(f"Drag and drop handling: {e}")
    time.sleep(1)

    # =========================================================================
    # 8. HANDLING IFRAMES
    # =========================================================================
    print("\n--- 8. HANDLING IFRAMES ---")
    open_url("https://practice.softwaretestingmentor.com/iframe")

    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Total iframes found -> {len(iframes)}")

    if len(iframes) > 0:
        # Switch to first iframe
        driver.switch_to.frame(iframes[0])
        print("Switched inside iframe 0 successfully!")
        time.sleep(1)
        # Return to main page content
        driver.switch_to.default_content()
        print("Switched back to main page content.")
    time.sleep(1)

    # =========================================================================
    # 9. FIND THE STATE OF A WEB ELEMENT (DISABLED AND ENABLED)
    # =========================================================================
    print("\n--- 9. FIND THE STATE OF A WEB ELEMENT ---")
    open_url("https://practice.softwaretestingmentor.com/login")

    user_box = driver.find_element(By.ID, "username")
    remember_cb = driver.find_element(By.CLASS_NAME, "remember-checkbox")

    print(f"Username Input Is Enabled?   -> {user_box.is_enabled()}")
    print(f"Username Input Is Displayed? -> {user_box.is_displayed()}")
    print(f"Remember me CB Is Selected?  -> {remember_cb.is_selected()}")
    time.sleep(1)

    # =========================================================================
    # 10. GET THE TEXT ON ELEMENT & GET VALUE OF ELEMENT ATTRIBUTE
    # =========================================================================
    print("\n--- 10. GET TEXT ON ELEMENT & GET VALUE OF ELEMENT ATTRIBUTE ---")

    heading = driver.find_element(By.TAG_NAME, "h2")
    print(f"Get Text on Element (.text)          -> '{heading.text}'")
    print(f"Get Value of 'id' Attribute          -> '{user_box.get_attribute('id')}'")
    print(f"Get Value of 'placeholder' Attribute -> '{user_box.get_attribute('placeholder')}'")
    time.sleep(2)

finally:
    driver.quit()