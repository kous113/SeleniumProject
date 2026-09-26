*** Settings ***
Documentation     Demonstrates Readable Gherkin-style Test Suite with User-Defined Keywords & Resources.
Resource          resources/common.resource
Test Setup        Log To Console    [SETUP] Starting Readable Test Case Execution...
Test Teardown     Close Application Session

*** Test Cases ***
Verify Example Domain Portal Gherkin Style
    [Documentation]    Verifies main heading on Example Domain using Gherkin syntax.
    [Tags]             readable    gherkin
    Given user opens the home page
    Then page heading should display "Example Domain"

*** Keywords ***
User opens the home page
    Navigate To Home Page

Page heading should display "${heading}"
    Verify Main Heading    ${heading}