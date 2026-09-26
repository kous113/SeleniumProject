# =========================================================================
# HANDLING DIFFERENT CONTROLS & XPATH DEMONSTRATION
# Syllabus Topics Covered:
# 1. XPath: Difference Between Absolute And Relative XPath
# 2. XPath using Contains Keyword, Starts-With Keyword, Parent & Sibling Nodes
# 3. Handling Button
# 4. Handling Input Box
# 5. Handling Checkbox
# 6. Handling Radio Button
# 7. Handling Select Box
# =========================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Initialize Chrome Driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    # =========================================================================
    # 1. XPATH: ABSOLUTE VS RELATIVE XPATH
    # =========================================================================
    print("\n--- 1. XPATH: ABSOLUTE VS RELATIVE XPATH ---")

    # Absolute XPath starts from root element (/html)
    abs_xpath_elem = driver.find_element(
        By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/header/div/div[2]/div[2]/div/div/div/div/h1"
    )
    print(f"Absolute XPath (from /html root): '{abs_xpath_elem.text}'")
    time.sleep(1)

    # Relative XPath starts anywhere in the document using double slash (//)
    rel_xpath_elem = driver.find_element(By.XPATH, "//input[@id='name']")
    print(f"Relative XPath (//input[@id='name']): ID = '{rel_xpath_elem.get_attribute('id')}'")
    time.sleep(1)

    # =========================================================================
    # 2. XPATH: CONTAINS, STARTS-WITH, PARENT & SIBLING NODES
    # =========================================================================
    print("\n--- 2. XPATH: CONTAINS, STARTS-WITH, PARENT & SIBLING NODES ---")

    # XPath using Contains Keyword: matches partial attribute or text
    contains_elem = driver.find_element(By.XPATH, "//input[contains(@id, 'email')]")
    print(f"XPath Contains Keyword: Located element ID -> '{contains_elem.get_attribute('id')}'")
    time.sleep(1)

    # XPath using Starts-With Keyword: matches starting text of an attribute
    starts_with_elem = driver.find_element(By.XPATH, "//input[starts-with(@id, 'phon')]")
    print(f"XPath Starts-With Keyword: Located element ID -> '{starts_with_elem.get_attribute('id')}'")
    time.sleep(1)

    # XPath Parent Node (/parent::*)
    parent_elem = driver.find_element(By.XPATH, "//input[@id='name']/parent::div")
    print(f"XPath Parent Node (/parent::div): Located container class -> '{parent_elem.get_attribute('class')}'")
    time.sleep(1)

    # XPath Following Sibling (/following-sibling::*)
    following_sibling = driver.find_element(By.XPATH, "//input[@id='male']/following-sibling::label")
    print(f"XPath Following Sibling (/following-sibling::label): Label text -> '{following_sibling.text}'")
    time.sleep(1)

    # XPath Preceding Sibling (/preceding-sibling::*)
    preceding_sibling = driver.find_element(By.XPATH, "//label[@for='female']/preceding-sibling::input")
    print(f"XPath Preceding Sibling (/preceding-sibling::input): Input ID -> '{preceding_sibling.get_attribute('id')}'")
    time.sleep(1)

    # =========================================================================
    # 3. HANDLING BUTTON
    # =========================================================================
    print("\n--- 3. HANDLING BUTTON ---")

    button_elem = driver.find_element(By.XPATH, "//button[contains(text(),'START')]")
    print(f"Button Text: '{button_elem.text}'")
    print(f"Button Enabled? -> {button_elem.is_enabled()}")
    print(f"Button Displayed? -> {button_elem.is_displayed()}")

    # Action: Click the button
    button_elem.click()
    print("Action: Clicked 'START' Button successfully!")
    time.sleep(1)

    # =========================================================================
    # 4. HANDLING INPUT BOX
    # =========================================================================
    print("\n--- 4. HANDLING INPUT BOX ---")

    input_box = driver.find_element(By.ID, "name")

    # Actions: clear, send_keys, and retrieve value
    input_box.clear()
    input_box.send_keys("John Doe")
    print(f"Action: Entered text into Input Box -> '{input_box.get_attribute('value')}'")
    time.sleep(1)

    # =========================================================================
    # 5. HANDLING CHECKBOX
    # =========================================================================
    print("\n--- 5. HANDLING CHECKBOX ---")

    checkbox = driver.find_element(By.ID, "sunday")
    print(f"Checkbox Initially Selected? -> {checkbox.is_selected()}")

    # Action: Click to select checkbox if not selected
    if not checkbox.is_selected():
        checkbox.click()

    print(f"Action: Clicked Checkbox! Is Selected Now? -> {checkbox.is_selected()}")
    time.sleep(1)

    # =========================================================================
    # 6. HANDLING RADIO BUTTON
    # =========================================================================
    print("\n--- 6. HANDLING RADIO BUTTON ---")

    radio_button = driver.find_element(By.ID, "male")
    print(f"Radio Button Initially Selected? -> {radio_button.is_selected()}")

    # Action: Click to select radio button if not selected
    if not radio_button.is_selected():
        radio_button.click()

    print(f"Action: Clicked Radio Button! Is Selected Now? -> {radio_button.is_selected()}")
    time.sleep(1)

    # =========================================================================
    # 7. HANDLING SELECT BOX (DROPDOWN)
    # =========================================================================
    print("\n--- 7. HANDLING SELECT BOX ---")

    select_element = Select(driver.find_element(By.ID, "country"))
    print(f"Total options in Select Dropdown -> {len(select_element.options)}")

    # Action 1: Select by Visible Text
    select_element.select_by_visible_text("Canada")
    print(f"Action 1: Selected option by text -> '{select_element.first_selected_option.text}'")
    time.sleep(1)

    # Action 2: Select by Value
    select_element.select_by_value("uk")
    print(f"Action 2: Selected option by value ('uk') -> '{select_element.first_selected_option.text}'")
    time.sleep(2)

finally:
    driver.quit()