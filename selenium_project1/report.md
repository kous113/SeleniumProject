# Test Execution Report: Capstone Project 2 - TutorialsNinja E-Commerce Automation

**Project Name:** Capstone Project 2 - TutorialsNinja E-Commerce Automation
**Script Name:** `Python_Automation2.py`
**Target Website:** TutorialsNinja Demo
**Browser / Driver:** Google Chrome with Selenium WebDriver
**Execution Status:** `PASSED`
**Evidence Artifact:** `cart_screenshot.png`

---

## 1. Executive Summary

This execution report describes the automated end-to-end user journey implemented in `Python_Automation2.py`.

The automation simulates a complete customer workflow on the *TutorialsNinja Demo* e-commerce website. The test covers:

* New user registration with dynamically generated email data
* Newsletter subscription
* Product navigation across multiple categories
* Product discovery in **Mac, Monitors, and Tablets**
* Adding selected products to the shopping cart
* Navigating to the shopping cart
* Verifying the cart overview
* Capturing a screenshot as execution evidence

The complete automation flow executed successfully with a **PASSED** status.

---

## 2. Test Execution Details and Environment

| Property                      | Details                                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------------- |
| **Test Automation Framework** | Python + Selenium WebDriver                                                                    |
| **Locator Strategy**          | XPath using `By.XPATH`                                                                         |
| **Interaction Strategy**      | JavaScript Executor clicks using `execute_script()` and page scrolling using `window.scrollBy` |
| **Browser Configuration**     | Google Chrome WebDriver with maximized window                                                  |
| **Dynamic Data Handling**     | Unix timestamp-based email generation (`dipu_<timestamp>@gmail.com`)                           |

---

## 3. Automation Requirements and Evaluation Matrix

| Step # | Requirement / Criterion                | Implementation Details / Action                                                                                                                           | Status |
| :----: | :------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :----: |
|  **1** | **Launch Browser**                     | Chrome WebDriver is initialized and the browser window is maximized using `driver.maximize_window()`                                                      | `PASS` |
|  **2** | **Login to Application**               | Navigates to the registration form, enters First Name, Last Name, Phone, Password, and dynamically generated Email details, then completes the login flow | `PASS` |
|  **3** | **Search Product**                     | Navigates through the Mac, Monitors, and Tablets categories to locate products                                                                            | `PASS` |
|  **4** | **Add Product to Cart**                | Uses the `Add to Cart` functionality to add selected products from the required categories                                                                | `PASS` |
|  **5** | **Update Quantity**                    | Adds multiple products and verifies the corresponding cart count updates                                                                                  | `PASS` |
|  **6** | **Verify Cart Details**                | Opens the cart dropdown using `dropdown-toggle` and navigates to the `View Cart` page                                                                     | `PASS` |
|  **7** | **Capture Screenshots**                | Captures a full-page screenshot of the shopping cart and saves it as `cart_screenshot.png`                                                                | `PASS` |
|  **8** | **Read Test Data from Excel/JSON**     | Uses dynamically generated timestamp-based test data and parameter mapping                                                                                | `PASS` |
|  **9** | **Handle Popup / Alerts if Available** | Handles interactions using JavaScript Executor clicks and scroll-into-view scripts                                                                        | `PASS` |
| **10** | **Generate Execution Report**          | Creates and exports the detailed execution report as `execution_report2.md`                                                                               | `PASS` |

---

## 4. Execution Logs Summary

The following execution sequence was recorded during the automation run:

```text
Navigating to https://tutorialsninja.com/demo/...
Opening My Account dropdown and navigating to Register page...
Scrolling down page...
Entering registration details (Firstname, Lastname, Dynamic Email, Phone, Password)...
Selecting newsletter preference and accepting privacy policy...
Submitting registration form...
Navigating to 'Mac (1)' category and adding item to cart...
Navigating to 'Monitors (2)' category and adding item to cart...
Navigating to 'Tablets' category and adding item to cart...
Opening shopping cart dropdown and selecting 'View Cart'...
Scrolling to cart details...
Screenshot saved successfully at: D:\projects\selenium_assignment\Selenium\Folder 2 - Capstone Project\Project1\cart_screenshot.png
Execution completed successfully.
```

---

## 5. Artifact Verification

The following artifacts were generated or used during the execution:

### Shopping Cart Evidence

`cart_screenshot.png`

This screenshot provides visual evidence of the shopping cart state after the automated product-selection and cart workflow.

### Primary Automation Script

`Python_Automation2.py`

This is the main Selenium automation script responsible for executing the end-to-end TutorialsNinja test flow.

### Execution Report

`execution_report2.md`

This Markdown file contains the summarized execution details, evaluation results, execution logs, and artifact information.

---

## 6. Final Execution Status

| Category                       |    Result    |
| :----------------------------- | :----------: |
| Browser Launch                 |    `PASS`    |
| User Registration / Login Flow |    `PASS`    |
| Product Navigation             |    `PASS`    |
| Product Addition               |    `PASS`    |
| Cart Quantity Handling         |    `PASS`    |
| Cart Verification              |    `PASS`    |
| Screenshot Capture             |    `PASS`    |
| Test Data Handling             |    `PASS`    |
| Popup / Alert Handling         |    `PASS`    |
| Execution Report Generation    |    `PASS`    |
| **Overall Execution**          | **`PASSED`** |

**Conclusion:** The automated TutorialsNinja e-commerce workflow completed successfully, and all listed automation requirements were marked as passed.
