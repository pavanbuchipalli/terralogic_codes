# import paramiko
# from paramiko.client import WarningPolicy
# from paramiko.client import SSHClient
#
# command = "df"
#
# host = "192.168.250.28"
# username  ="pavan"
# password  ="yugesh@05"
#
# client = paramiko.client.SSHClient
# client.set_missing_host_key_policy(WarningPolicy())
# client.connect(host,username=str(username), password=str(password))
# _stdin,_stdout,_stderr = client.exec_command("df")
# print(_stdout.read().decode())
# client.connect()


import subprocess





run

