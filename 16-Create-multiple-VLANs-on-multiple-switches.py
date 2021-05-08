import getpass
import telnetlib

# Since my credentials for all four switches are same, i let the user prompt to enter the password at the beginning of the code. If the credentials are different for each switches, put the code insde the for loop 

user=input("Enter your username :")
password = getpass.getpass()

# Load and open the switches.txt file in the code
f = open("switches.txt")

# for loop will get the IP from the switches.txt file one by one and execute the code block. Once again, please note the indentations.

for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.wrtie(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    # use for loop to create VLANs in range 2:10 (The end is Data_VLAN_9)
    for n in range(2, 10):
        tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
        tn.write(b"name Data_VLAN_" + str(n).encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan br\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
