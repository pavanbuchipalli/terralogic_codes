*** Settings ***
Library           SeleniumLibrary
*** Test Cases ***
first_test_case

    Open Browser    https://terralogic.paxanimi.ai/login   chrome
    Maximize Browser Window
    Sleep    3s
    Click Element    Xpath://button[@type="button"]
    Sleep    3s
    ${handles}=     Get Window Handles
#    Switch Window    Sign in - Google Accounts
    Switch Window    ${handles}[1]
    Sleep   3s
    Click Element    Xpath://input[@type="email"]
    Input Text    Xpath://input[@type="email"]      pavan.buchipalli@terralogic.com

    Click Element    Xpath://span[text()='Next']
    sleep   3s
    Input Text    Xpath://input[@type="password"]       Yugesh@05
    sleep   3s
    Click Element    Xpath://span[text()='Next']/..
    Sleep     50s
    Switch Window       ${handles}[0]
    ${title}        Get Title
    Log To Console    ${title}
     Click Element    Xpath:(//span[@class="ant-menu-title-content"]/a)[2]
    Sleep    3s
    Mouse Out    Xpath:(//span[@class="ant-menu-title-content"]/a)[2]
    Sleep    3s
    ${count}    Get Element Count    Xpath://img[contains(@src, '/static/timesheetCheck.bf9bab90.svg')]
    Sleep    3s
    Log To Console    Total no of days timesheet filled this month ${count}


