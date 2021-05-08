import getpass
import telnetlib

user = input("Enter your username :")
password = getpass.getpass()

f = open("switches.txt")
for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(user.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write("cisco")
    tn.write(b"conf t\n")
    tn.write(b"ip domain-name sai-digital.com\n")
    tn.write(b"crypto key generate rsa modules 1024\n\n")
    tn.write(b"line vty 0 4\n")
    tn.write(b"transport input ssh telnet\n")
    tn.write(b"end\n")
    tn.write(b"write memory\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))