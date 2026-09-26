*** Settings ***
Documentation     Common Resource File containing reusable user keywords and variables.
Library           SeleniumLibrary

*** Variables ***
${BASE_URL}       https://example.com
${BROWSER}        headlesschrome

*** Keywords ***
Navigate To Home Page
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Verify Main Heading
    [Arguments]    ${expected_heading}
    Page Should Contain    ${expected_heading}

Close Application Session
    Close All Browsers