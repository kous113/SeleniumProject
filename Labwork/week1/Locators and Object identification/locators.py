

# =========================================================================
# NEW IMPLEMENTATION: PRACTICE SOFTWARE TESTING MENTOR
# Website: https://practice.softwaretestingmentor.com/login
# =========================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

try:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://practice.softwaretestingmentor.com/login")
    time.sleep(3)  # Wait for page load

    # =========================================================================
    # 1. FIND ELEMENT BY ID AND NAME
    # =========================================================================
    print("\n--- 1. FIND ELEMENT BY ID AND NAME ---")

    # Locate Username by ID and type 'admin'
    username_field = driver.find_element(By.ID, "username")
    username_field.clear()
    username_field.send_keys("admin")
    print(f"By ID ('username'): Entered username -> '{username_field.get_attribute('value')}'")
    time.sleep(1)

    # Locate Password by Name and type 'password123'
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("password123")
    print(f"By Name ('password'): Entered password -> '{password_field.get_attribute('value')}'")
    time.sleep(1)

    # =========================================================================
    # 2. BY TAG NAME, LINK TEXT, CLASS NAME (THREE OPERATIONS)
    # =========================================================================
    print("\n--- 2. BY TAG NAME, LINK TEXT, CLASS NAME (THREE OPERATIONS) ---")

    # Operation 1: By Class Name - Locate 'Remember Me' Checkbox and Click it
    remember_checkbox = driver.find_element(By.CLASS_NAME, "remember-checkbox")
    remember_checkbox.click()
    print(f"1. By Class Name ('remember-checkbox'): Clicked 'Remember me' checkbox (Checked: {remember_checkbox.is_selected()})")
    time.sleep(1)

    # Operation 2: By Tag Name - Locate Sign In Button using ONLY Tag Name ("button") and Click it
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        if "Sign In" in btn.text:
            btn.click()
            print(f"2. By Tag Name ('button'): Located 'Sign In' button using ONLY TAG_NAME and clicked it!")
            break
    time.sleep(1)

    # Operation 3: By Link Text - Find 'Register here' Text and Click it
    register_link = driver.find_element(By.LINK_TEXT, "Register here")
    print(f"3. By Link Text ('Register here'): Located text -> '{register_link.text}'")
    register_link.click()
    print("   Successfully clicked 'Register here' link!")
    time.sleep(2)

    # Operation 4: By Link Text - Click 'Sign in' link to return to Login page
    signin_link = driver.find_element(By.LINK_TEXT, "Sign in")
    print(f"4. By Link Text ('Sign in'): Located text -> '{signin_link.text}'")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", signin_link)
    time.sleep(1)
    signin_link.click()
    print("   Successfully clicked 'Sign in' link!")
    time.sleep(2)

    # =========================================================================
    # 3. FIND LIST OF ELEMENTS (find_elements)
    # =========================================================================
    print("\n--- 3. FIND LIST OF ELEMENTS ---")

    # Locate list of all form-control input elements
    input_list = driver.find_elements(By.CLASS_NAME, "form-control")
    print(f"Find List of Elements (find_elements): Found {len(input_list)} input fields.")

    for idx, item in enumerate(input_list, start=1):
        print(f"   Element {idx}: ID = '{item.get_attribute('id')}', Name = '{item.get_attribute('name')}'")
    time.sleep(1)

    # =========================================================================
    # 4. BY CSS, WILDCARDS WITH CSS SELECTORS, CHILD NODES USING CSS SELECTORS
    # =========================================================================
    print("\n--- 4. BY CSS, WILDCARDS, AND CHILD NODES ---")

    # 4a. Basic CSS Selector (input#username)
    username_css = driver.find_element(By.CSS_SELECTOR, "input#username")
    print(f"Basic CSS Selector ('input#username'): Located element ID -> '{username_css.get_attribute('id')}'")
    time.sleep(1)

    # 4b. CSS Wildcard ^= (Starts With 'user')
    starts_with = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
    print(f"CSS Wildcard ^= (Starts with 'user'): Located element ID -> '{starts_with.get_attribute('id')}'")
    time.sleep(1)

    # 4c. CSS Wildcard $= (Ends With 'word')
    ends_with = driver.find_element(By.CSS_SELECTOR, "input[id$='word']")
    print(f"CSS Wildcard $= (Ends with 'word'): Located element ID -> '{ends_with.get_attribute('id')}'")
    time.sleep(1)

    # 4d. CSS Wildcard *= (Contains 'sswor')
    contains = driver.find_element(By.CSS_SELECTOR, "input[id*='sswor']")
    print(f"CSS Wildcard *= (Contains 'sswor'): Located element ID -> '{contains.get_attribute('id')}'")
    time.sleep(1)

    # 4e. CSS Child Nodes - Direct Child (>)
    direct_child = driver.find_element(By.CSS_SELECTOR, "div.form-group > input#username")
    print(f"CSS Direct Child Node ('div.form-group > input#username'): Located ID -> '{direct_child.get_attribute('id')}'")
    time.sleep(1)

    # 4f. CSS Child Nodes - Descendant (Space)
    descendant = driver.find_element(By.CSS_SELECTOR, "form input#password")
    print(f"CSS Descendant Node ('form input#password'): Located ID -> '{descendant.get_attribute('id')}'")
    time.sleep(2)

finally:
    driver.quit()