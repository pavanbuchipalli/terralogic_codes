*** Settings ***
Library    SeleniumLibrary
Resource    ../varaibles/login_varaibles.robot
Resource    ../keywords/common_keywords.robot

*** Keywords ***
Launch HROS Browser
	Open Application    ${url_hros}

Click Terralogic Button
    Click Buttons        ${click_terralogic}

Enter emailids and Passwords
	Enter emailid and Password  ${emilid_hros}   ${password_hros}   ${email_hros}   ${passwords_hros}

manger_data
	Click_on_manager    ${manager_xapath}

moveout_on_manager
	move_on_manager     ${manager_xapath}

get_manager_name
	${c}=   Get_name    ${manager_name}
	[RETURN]   ${c}

get_employee_name
    ${s}=   Get_name    ${employee_name}
    [Return]       ${s}

Concatenate Keywords and Log Message
    ${result1} =    Run Keyword    Get_name    ${employee_name}
    ${result2} =    Run Keyword    Get_name    ${manager_name}
    Log To Console        ${result1} is working under ${result2}

dashboaed_click
	Click Buttons    ${dashboard}

timesheet_click
	click_on_element    ${timesheet_xpath}
move_out_timesheet
	move_on_manager      ${timesheet_xpath}

get_total_filled_values
	${R}=   Get_count    ${data_filled_xpath}
	Log To Console    Total Number of days timesheet filled this month is ${R}




