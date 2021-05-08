# import the necessary library files using import command.
import getpass
import telnetlib

# Declare a variable for storing the IP address
IP = "192.168.122.20"
# Declare a variable for storing username
user =  input("Enter your username :")
# Use getpass module which we imported, to get the password from the user
password = getpass.getpass()
#Pass the IP variable value in to the telnetlib which we imported
tn = telnetlib.Telnet(IP)

# Python code works top to bottom. Now the code will read each output from the cisco switch and when it encounter the Username: statement, do the following
tn.read_until(b"Username: ")
# Remember, python3 by default uses unicode encodeing. Here we have to use the ascii encoding because this has to be send to the switch as ascii characters.
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_util(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
# Now specify the commands in the right sequence.enable password, then change to configuration terminal and change the hostname, finally save the configuration and exit
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"hostname CoreSW\n")
tn.write(b"end\n")
tn.write(b"write memory\n")
# read_all() function will show the output on your screen after decoding the ascii to unicode.
print(tn.read_all().decode('ascii'))