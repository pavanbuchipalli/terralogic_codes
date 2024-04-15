*** Settings ***
Library    SSHLibrary
Library    Collections
Library    BuiltIn
Library    String
Library    Process
Library    OperatingSystem
Library    P
Library    SSHLibrary
Library    Collections
Library    BuiltIn
Library    String
Library    Process
Library    OperatingSystem
Library    psutil



*** Variables ***
${HOSTNAME}    192.168.1.13
${USERNAME}    pavan
${PASSWORD}    password
${SCRIPT_NAME}    tem
${PROCESS_TIMEOUT}      15m
${path}        /home/pavan/
${local_path}       C:\Users\PavanB-3247\PycharmProjects\pythonProject\2)assignment_palindrome

*** Test Cases ***
Create and Run Script and Get PID
    # Connect to the remote server
    Open Connection    ${HOSTNAME}
    Login    ${USERNAME}    ${PASSWORD}



Get system information\n
    ${username}=    Execute Command    whoami
    ${id}=    Execute Command    id -u
    ${top_processes}=    Execute Command    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6
    Log To Console   Remote server username is ${username}
    Log To Console    Remote server id is ${id}
    Log To Console    ${top_processes}





    ${pid}    Start Command    python3 /home/pavan/tem.py &>/dev/null & echo $!

    # Wait for the task to start
    Wait Until Keyword Succeeds    10s    1s    Process Should Be Running    ${pid}


    Log To Console    ${pid}

    # Get the CPU and memory usage of the task
#    ${cpu_usage}    Get Process CPU Usage    ${pid}
#    ${mem_usage}    Get Process Memory Usage    ${pid}
#
#    # Print the CPU and memory usage
#    Log    CPU usage: ${cpu_usage}
#    Log    Memory usage: ${mem_usage}


#
#    Put File    ${local_path}    ${path}
#
#    # Run the Python file on the remote server
#    ${output}=   Execute Command    python3 ${path}

    # Print the output of the Python file
#    Log To Console       ${output}


    #Check Sleep Command Status



#Check Sleep Command Status
#    ${sleep_process}    Start Process    sleep    300
#    FOR    ${i}    IN RANGE    10
#        Sleep    10
#        TRY
#            ${process}    Get Process    ${sleep_process.pid}
#            ${status}    ${_}    ${_}    ${_}    ${_}    ${_}    ${_}    ${_}    ${_}    ${process.status()}
#            Log    Sleep command status: ${status}
#            Run Keyword If    '${status}' == 'zombie'    Terminate Process    ${sleep_process.pid}
#            Run Keyword Unless    '${status}' == 'sleeping'    Fail    Sleep command not sleeping
#        EXCEPT
#            psutil.NoSuchProcess
#            Log    Sleep command process not found
#    Run Keyword If    '${sleep_process.poll()}' is None    Terminate Process    ${sleep_process.pid}
#



#    Execute Command       cd ${path}
#    ${pwd}=   Execute Command    pwd
#    Log To Console    ${pwd}
#
#
#    Execute Command    python3 tem.py &
#    ${ps u}=    Execute Command
#    Log To Console    ${ps u}

#    ${command}=      Set Variable    python3 ${SCRIPT_NAME} &
#
#    Execute Command    ${command}
#
##    Wait Until Keyword Succeeds    3x 1s    Execute Command    ${pid_command}
#    ${outpu}=       Execute Command     ps aux |grep ${path} |grep -v grep
#
#    ${pid}=     Run Keyword If    '${output}' != ''
#    Log To Console    ${pid}




#    # Execute the Python file on the remote server in the background and capture its PID
#    ${pid_output}    Execute Command    python3 ${SCRIPT_NAME}.py &
#    ${pid}=    Run Keyword And Return Status    pidof python3
#
#    # Log the PID of the Python process on the remote server
#    Log To Console       The PID of the Python process on the remote server is ${pid}
#
#    # Close the SSH connection
    Close Connection






























