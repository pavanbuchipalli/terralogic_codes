import paramiko
import subprocess
import ass

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.250.28",username="pavan",port =22,password="Yugesh@05")
#sftp_client=ssh.open_sftp()
subprocess.Popen(["python", "assig66.py"])

subprocess.Popen(["sleep -300"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# stdin,stdout,stderr=ssh.exec_command()
# print(stdout.read().decode())

ssh.close()

