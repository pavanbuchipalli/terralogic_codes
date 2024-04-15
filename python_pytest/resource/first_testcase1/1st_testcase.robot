#
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
    sleep  15s
    Switch Window    ${handles}[0]
    ${title}        Get Title
    sleep   10s
    Log To Console    ${title}
    Close Browser
