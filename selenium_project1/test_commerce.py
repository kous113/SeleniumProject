from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json

driver = webdriver.Chrome()

try:
    # --------------------------------
    # Read test data from JSON
    # --------------------------------
    project_folder = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(
        project_folder,
        "data",
        "testdata.json"
    )

    with open(data_path, "r") as file:
        testdata = json.load(file)

    # --------------------------------
    # Open Website
    # --------------------------------
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    time.sleep(3)

    # --------------------------------
    # Step 1: Registration
    # --------------------------------
    account_dropdown = driver.find_element(
        By.XPATH,
        "//i[@class='fa fa-user']"
    )
    account_dropdown.click()
    time.sleep(1)

    registration = driver.find_element(
        By.XPATH,
        "//a[normalize-space()='Register']"
    )
    registration.click()
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(1)

    firstname = driver.find_element(
        By.XPATH,
        "//input[@id='input-firstname']"
    )
    firstname.send_keys(testdata["first_name"])
    time.sleep(1)

    lastname = driver.find_element(
        By.XPATH,
        "//input[@id='input-lastname']"
    )
    lastname.send_keys(testdata["last_name"])
    time.sleep(1)

    email = driver.find_element(
        By.XPATH,
        "//input[@id='input-email']"
    )
    email.send_keys(
        f"{testdata['first_name'].lower()}_{int(time.time())}@gmail.com"
    )
    time.sleep(1)

    telephone = driver.find_element(
        By.XPATH,
        "//input[@id='input-telephone']"
    )
    telephone.send_keys(testdata["mobile_number"])
    time.sleep(1)

    password = driver.find_element(
        By.XPATH,
        "//input[@id='input-password']"
    )
    password.send_keys(testdata["password"])
    time.sleep(1)

    confirm_password = driver.find_element(
        By.XPATH,
        "//input[@id='input-confirm']"
    )
    confirm_password.send_keys(testdata["password"])
    time.sleep(1)

    subscribe = driver.find_element(
        By.XPATH,
        "(//input[@name='newsletter'])[1]"
    )
    subscribe.click()
    time.sleep(1)

    policy = driver.find_element(
        By.XPATH,
        "//input[@name='agree']"
    )
    policy.click()
    time.sleep(1)

    continue_button = driver.find_element(
        By.XPATH,
        "//input[@value='Continue']"
    )
    continue_button.click()
    time.sleep(1)

    # --------------------------------
    # Step 2: Add Mac to Cart
    # --------------------------------
    mac_find = driver.find_element(
        By.XPATH,
        "//a[normalize-space()='Mac (1)']"
    )
    driver.execute_script(
        "arguments[0].click();",
        mac_find
    )
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(1)

    addtocart_mac = driver.find_element(
        By.XPATH,
        "//span[normalize-space()='Add to Cart']"
    )
    driver.execute_script(
        "arguments[0].click();",
        addtocart_mac
    )
    time.sleep(1)

    # --------------------------------
    # Step 3: Add Tablet to Cart
    # --------------------------------
    tablet_find = driver.find_element(
        By.XPATH,
        "//ul[@class='nav navbar-nav']//a[contains(text(),'Tablets')]"
    )
    driver.execute_script(
        "arguments[0].click();",
        tablet_find
    )
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(1)

    addtocart_tablet = driver.find_element(
        By.XPATH,
        "//span[normalize-space()='Add to Cart']"
    )
    driver.execute_script(
        "arguments[0].click();",
        addtocart_tablet
    )
    time.sleep(1)

    # --------------------------------
    # Step 4: View Cart
    # --------------------------------
    view_cart = driver.find_element(
        By.XPATH,
        "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']"
    )
    driver.execute_script(
        "arguments[0].click();",
        view_cart
    )
    time.sleep(1)

    view_cart = driver.find_element(
        By.XPATH,
        "//strong[normalize-space()='View Cart']"
    )
    driver.execute_script(
        "arguments[0].click();",
        view_cart
    )
    time.sleep(1)

    # --------------------------------
    # Step 5: Update Quantity
    # --------------------------------
    quantity_tab = driver.find_element(
        By.XPATH,
        "(//input[contains(@name, 'quantity')])[1]"
    )
    quantity_tab.clear()
    quantity_tab.send_keys(testdata["quantity"])
    time.sleep(1)

    update_cart = driver.find_element(
        By.XPATH,
        "(//button[@data-original-title='Update' or i[contains(@class, 'fa-refresh')]])[1]"
    )
    driver.execute_script(
        "arguments[0].click();",
        update_cart
    )
    time.sleep(1)

    # --------------------------------
    # Step 6: Screenshot
    # --------------------------------
    driver.execute_script("window.scrollBy(0, 350);")
    time.sleep(1)

    screenshot_folder = os.path.join(
        project_folder,
        "screenshots"
    )

    screenshot_path = os.path.join(
        screenshot_folder,
        "cart_screenshot.png"
    )

    driver.save_screenshot(screenshot_path)

    print(
        f"Screenshot saved successfully at: {screenshot_path}"
    )

finally:
    driver.quit()