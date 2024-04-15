*** Settings ***
Library    SeleniumLibrary
Resource    ../testcases/firstpo.robot

*** Test Cases ***
Automating login Hros
	Launch HROS Browser
	Maximize Browser Window
    sleep  3s
    Click Terralogic Button
    Sleep    3s
    ${handles}=     Get Window Handles
    Switch Window    ${handles}[1]
    Sleep   3s
    Log To Console    ${handles}
    Enter Emailids And Passwords
    Sleep    3s
    Switch Window    ${handles}[0]
    sleep  25s
    ${title}        Get Title
    Log To Console    ${title}
    Sleep    30s
    timesheet_click
    sleep   3s
    move_out_timesheet
    sleep   3s
    FOR    ${i}    IN RANGE    1    6
        Click Element    xpath:(//img[contains(@src, '/static/timesheetCheck.bf9bab90.svg')])[${i}]
        Sleep    3s
#        Click Element    xpath://button[@type="button"]//div[text()='Add Task']
#        Sleep    3s
#        Click Element    Xpath: id:basic_tasks_0_projectId
#        Sleep    3s
#        Input Text      Xpath: id:basic_tasks_0_projectId       rampup
#        Sleep    3s
#        Press Key       Xpath://div[text()='Rampup_Software Services - Terralogic']      ENTER
#        Sleep    3s
#        Input Text      Xpath://textarea[@placeholder='Enter the description']      hellovhc
#        Sleep    3s
#        Click Element       Xpath://div[text()='Submit']
        Sleep    10
        Go Back
        Sleep    7s
    END


#    get_total_filled_values
#    Sleep    3s
#
