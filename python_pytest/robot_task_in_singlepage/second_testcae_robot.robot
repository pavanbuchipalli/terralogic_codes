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
    Sleep    3s
    Click Element    Xpath:(//span[@class="ant-menu-title-content"]/a)[3]
    Sleep    10s
#    ${handles2}=     Get Window Handles
#    Log To Console    ${handles2}
    sleep   5s
    Mouse Out       Xpath:(//span[@class="ant-menu-title-content"]/a)[3]
    sleep   3s


    ${manager}=     Get Text    Xpath:(//div[@id="625764aececaa30012bed3ee"]/div)[1]/div/div[2]
    Sleep    3s
    ${employee}=    Get Text    Xpath:(//div[@id="6433d492f27e0315d9a73106"]/div)[1]/div/div[2]
    Log To Console    hey ${employee} you are working under ${manager}

