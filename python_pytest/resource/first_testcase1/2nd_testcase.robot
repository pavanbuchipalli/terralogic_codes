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
    sleep  3s
    ${title}        Get Title
    Log To Console    ${title}
    Sleep    15s
    manger_data
    Sleep    10s
    moveout_on_manager
    sleep   3s
    get_manager_name
    Sleep    3s
    get_employee_name
    Concatenate Keywords and Log Message
    Close Browser

