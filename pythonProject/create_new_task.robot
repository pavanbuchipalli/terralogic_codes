*** Settings ***
Library    SSHLibrary
Library    Collections
Library    BuiltIn
Library    String
Library    Process
Library    OperatingSystem
*** Variables ***
${HOSTNAME}    192.168.250.84
${USERNAME}    pavan
${PASSWORD}    password
${path}        /home/pavan/pavan32l.py
${data}         import time\nfor i in range(1,100):\n\ttime.sleep(i)
${count}         0
*** Test Cases ***
Create and Run Script and Get PID
    # Connect to the remote server
    Open Connection    ${HOSTNAME}
    Login    ${USERNAME}    ${PASSWORD}
Get system information\n
    # This will Fetch the username of the remote server
    ${username}=    Execute Command    whoami
    # This will Fetch the ID  of the remote server
    ${id}=    Execute Command    id -u
    # This will Fetch the top cpu and mem process  of the remote server
    ${top_processes}=    Execute Command    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6
    Log To Console   Remote server username is ${username}
    Log To Console    Remote server id is ${id}
    Log To Console    ${top_processes} 
    #This will create new task in remote server
    Execute Command    touch ${path}    shell=True
    #This comand will append the data into the file
    Execute Command    echo "${data}" > ${path}
    #This will change the mode of the file
    Execute Command    chmod +x ${path}
    #To run the file in the background
    ${background}=         Set Variable    nohup python3 ${path} > output.log 2>&1 &
    ${stdout}=          Execute Command    ${background}
    ${taskmanager}=      Set Variable    ps aux | grep ${path} | grep -v grep
    ${output}=          Execute Command    ${taskmanager}

    #This will give the pid number of the process
    ${pid}=             Set Variable    ${output.split()[1]}
    Log To Console      Process ID of new task is : ${pid}

    #This command will provide cpu and mem Usage of the process
    ${cpu_mem}=     Execute Command    ps -p ${pid} -o %cpu,%mem,cmd
    Log To Console    Cpu and mem Usage of new task is \n ${cpu_mem}

    #This will kill the process with Given  pid number
    Execute Command    kill -9 ${pid}
    ${ps_out}           Set Variable    ps aux |grep ${pid}

    ${pout}=        Execute Command    ${ps_out}

    FOR    ${i}  IN  @{pout.splitlines()}
        IF    ${i.split()[1]} == ${pid}
            ${count}=  ${count} + 1
        END
    END

    IF    ${count} == 0
        Log To Console    The process with pid ${pid} is killed
    ELSE
        Log To Console    The process with ${pid} is not killed
    END

#    ${kill}=        Execute Command     kill -9 ${PID} || True
#
#    Log To Console    ${kill}
