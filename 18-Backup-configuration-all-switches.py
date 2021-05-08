import getpass
import telnetlib

user = input("Enter your username :")
password = getpass.getpass()

f = open("switches.txt")
for IP in f:
    #IP.strip() is used here to remove if any white-spaces contained in the IP addresses
    IP = IP.strip()
    print("Taking backup of Switch " + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    # terminal length 0 command eliminate the need to press enter key to show more configuration portion
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    # read all the output of the operations to a variable named as output
    output = tn.read_all()
    # opening a file SW+IP address with write permission
    config = open("SW" + IP, "w")
    config.write(output.decode("ascii"))
    config.write("\n")
    # close the files opened
    config.close
print(tn.read_all().decode("ascii"))