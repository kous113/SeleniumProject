*** Settings ***
Documentation     Simple Robot Framework Test Suite Demonstrating Setup, Keywords, and Data-Driven Tests.
Library           SeleniumLibrary

*** Variables ***
${URL}            https://example.com
${BROWSER}        headlesschrome

*** Test Cases ***
Verify Example Domain Homepage Title
    [Documentation]    Verifies page title and heading on Example Domain website.
    [Tags]             smoke
    Open Browser To Page
    Verify Page Title
    Close Browser Session

*** Keywords ***
Open Browser To Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Verify Page Title
    Title Should Be    Example Domain
    Page Should Contain    Example Domain

Close Browser Session
    Close Browser