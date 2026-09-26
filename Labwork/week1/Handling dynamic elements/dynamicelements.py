# =========================================================================
# IMPLEMENTATION: PRACTICE SOFTWARE TESTING MENTOR
# Website: https://practice.softwaretestingmentor.com/dynamic-table
# Syllabus Topics Covered:
# 1. Working with WebTable
# 2. Traversing through WebTable
# =========================================================================

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options to handle anti-bot checks smoothly
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
    print("=================================================================")
    print("HANDLING DYNAMIC ELEMENTS - WORKING WITH & TRAVERSING WEBTABLE")
    print("Website: https://practice.softwaretestingmentor.com/dynamic-table")
    print("=================================================================\n")

    # 1. Open WebTable Page
    open_url("https://practice.softwaretestingmentor.com/dynamic-table")

    # Locate the WebTable
    table = driver.find_element(By.ID, "dynamic-table")
    print("WebTable located successfully!")

    # =========================================================================
    # 1. WORKING WITH WEBTABLE (COUNT ROWS, COLUMNS & HEADERS)
    # =========================================================================
    print("\n--- 1. WORKING WITH WEBTABLE ---")
    
    # Locate all rows (including table body rows)
    all_rows = driver.find_elements(By.XPATH, "//table[@id='dynamic-table']//tr")
    total_rows = len(all_rows)

    # Locate all table header columns
    header_cols = driver.find_elements(By.XPATH, "//table[@id='dynamic-table']//th")
    total_cols = len(header_cols)

    print(f"Total Table Rows (Header + Data): {total_rows}")
    print(f"Total Table Columns: {total_cols}")

    # Extract Header Text
    headers = [col.text.split('\n')[0].strip() for col in header_cols]
    print(f"Table Headers: {headers}")

    # =========================================================================
    # 2. TRAVERSING THROUGH WEBTABLE (ROW BY ROW & CELL BY CELL)
    # =========================================================================
    print("\n--- 2. TRAVERSING THROUGH WEBTABLE ---")

    # Body rows (excluding header)
    body_rows = driver.find_elements(By.XPATH, "//table[@id='dynamic-table']/tbody/tr")
    
    print("\nIterating through each row and printing cell data:")
    for r_idx, row in enumerate(body_rows, start=1):
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_data = [cell.text.strip() for cell in cells]
        print(f"Row {r_idx}: {cell_data}")

    # =========================================================================
    # 3. CONDITIONAL SEARCH & DATA EXTRACTION IN WEBTABLE
    # =========================================================================
    print("\n--- 3. CONDITIONAL SEARCH IN WEBTABLE ---")
    
    # Search for employees in 'Engineering' Department
    print("Employees in 'Engineering' Department:")
    for r_idx, row in enumerate(body_rows, start=1):
        dept = driver.find_element(By.XPATH, f"//table[@id='dynamic-table']/tbody/tr[{r_idx}]/td[3]").text.strip()
        if dept == "Engineering":
            name = driver.find_element(By.XPATH, f"//table[@id='dynamic-table']/tbody/tr[{r_idx}]/td[2]").text.strip()
            salary = driver.find_element(By.XPATH, f"//table[@id='dynamic-table']/tbody/tr[{r_idx}]/td[4]").text.strip()
            print(f"  -> Name: {name} | Salary: {salary}")

    # =========================================================================
    # 4. SUMMING / PROCESSING NUMERIC VALUES FROM WEBTABLE
    # =========================================================================
    print("\n--- 4. PROCESSING NUMERIC COLUMN VALUES (SALARY SUM) ---")
    
    total_salary = 0
    for r_idx in range(1, len(body_rows) + 1):
        salary_str = driver.find_element(By.XPATH, f"//table[@id='dynamic-table']/tbody/tr[{r_idx}]/td[4]").text.strip()
        # Clean salary string e.g. "$95,000" -> 95000
        clean_salary = int(salary_str.replace("$", "").replace(",", ""))
        total_salary += clean_salary
    
    print(f"Total Salary of All Employees in Table: ${total_salary:,}")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser Session Closed Successfully.")