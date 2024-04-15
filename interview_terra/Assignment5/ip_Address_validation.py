


import re
import subprocess

# ip = "192.22.23.225"
# ip = "24.12.86.216"
# ip ="60.233.161.149"
class ip_():
    def ping_valid(self):
        while True:
            ip = input("provide a valid input :----")
            check = input("Do you want to check this ip address -- ({}) -- and ping it  select yes/no".format(ip))
            if check == "yes":
                pattern = r"^(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

                match = re.match(pattern, ip)

                if match:
                    ip_to_ping = match.group()  # Extract the matched IP address
                    try:
                        output = subprocess.check_output(['ping', ip_to_ping])
                        ping_result = output.decode('utf-8')
                        print(ping_result)
                        files = open("ip_check", "a")
                        files.write("valid_ip:   "  +  ip_to_ping + "\n")

                    except subprocess.CalledProcessError as e:
                        print(e.output.decode('utf-8'))
                        files = open("ip_check", "a")
                        files.write("invalid_ip    :"  +  ip_to_ping + "\n")


                else:
                    print("Invalid IP address format")
            else:
                file3 =open("ip_check","r")
                print("list of valid and invalid ips","\n",file3.read())

obj =ip_()
obj.ping_valid()