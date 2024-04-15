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

    Switch Window    ${handles}[1]
    Sleep   3s
    Click Element    Xpath://input[@type="email"]
    Input Text    Xpath://input[@type="email"]      @terralogic.com

    Click Element    Xpath://span[text()='Next']
    sleep   3s
    Input Text    Xpath://input[@type="password"]       nnnnnn
    sleep   3s
    Click Element    Xpath://span[text()='Next']/..
    Sleep     50s
    Switch Window       ${handles}[0]
    ${title}        Get Title
    Log To Console    ${title}
