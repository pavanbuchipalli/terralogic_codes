import paramiko
import subprocess

ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.250.28",username="pavan",port =22,password="Yugesh@05")
# sftp_client=ssh.open_sftp()
stdin,stdout,stderr=ssh.exec_command("whoami")
print("User name  :-",stdout.read().decode())
stdin,stdout,stderr=ssh.exec_command("id")
print("current id   :-",stdout.read().decode())
stdin,stdout,stderr=ssh.exec_command("ps aux --sort -%cpu")
print("cpu and memory use\n", stdout.read().decode())

v= stdout.read().decode()

split_lines=v.splitlines()

columns_list=split_lines[0].split()
cpu_index=columns_list.index('%CPU')
cpu=[]
for i in range(1,len(split_lines)):
    split_each_line=split_lines[i].split()
    cpu.append(float(split_each_line[cpu_index]))
maximum_cpu=max(cpu)
print(maximum_cpu)
memory_index=columns_list.index('%MEM')

mem=[]
for i in range(1,len(split_lines)):
    split_each_line=split_lines[i].split()
    mem.append(float(split_each_line[memory_index]))

#print(mem)
maximum_mem=max(mem)
print(maximum_mem)
for i in range(1,len(split_lines)):
    split_each_line=split_lines[i].split()
    if str(maximum_cpu) in split_each_line and str(maximum_mem) in split_each_line:
        print("maximum %CPU %MEM",split_each_line)










ssh.close()
