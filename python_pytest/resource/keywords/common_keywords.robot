*** Settings ***
Library    SeleniumLibrary
Resource    ../varaibles/login_varaibles.robot

*** Keywords ***
Open Application
	[Arguments]    ${url}
    Open Browser    ${url}    Chrome

Click Buttons
	[Arguments]    ${Button_xpath}
	Click Button    ${Button_xpath}

Enter emailid and Password
	[Arguments]    ${username}     ${password}  ${u_xpath}  ${p_xpath}
	Input Text    xpath:${u_xpath}      ${username}
	sleep  5s
    Click Buttons   ${next_email_hros}
    sleep  5s
	Input Text    xpath:${p_xpath}      ${password}
	Click Buttons    ${next_password_hros}

click_on_element
	[Arguments]    ${element_path}
	Click Element    Xpath:${element_path}

click_on_manager
	[Arguments]    ${managesr}
	Click Element    Xpath:${managesr}
move_on_manager
    [Arguments]    ${managesr}
	Mouse Out       Xpath:${managesr}
get_name
	[Arguments]    ${name_xpath}
	${getting_value}=      Get Text    Xpath:${name_xpath}
	[Return]    ${getting_value}

get_count
	[Arguments]     ${count_xapth}
	${get_count_number}    Get Element Count        Xpath:${count_xapth}
	[Return]    ${get_count_number}