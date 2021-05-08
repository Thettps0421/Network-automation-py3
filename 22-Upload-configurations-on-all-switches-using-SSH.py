## Following changes to all the three switches
# 1 Create a new user
# 2 Assign an NTP server
# 3 Enable 4 ports and assign them an access VLAN
# 4 Save the configurations.
## Created a file named as config_change.txt with all the required commands.
## onece need created the file, use cat command to view the contents.
from netmiko import ConnectHandler

switch1 = {
    'devices': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
}

switch2 = {
    'devices': 'cisco_ios',
    'ip': '192.168.122.22',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
}

switch3 = {
    'devices': 'cisco_ios',
    'ip': '192.168.122.23',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
}

switches = [switch1, switch2, switch3]

# open the config_change.txt file that has all the commands that we need to execute and read lines
with open('config_change.txt') as f:
    lines = f.read().splitlines()
    print(lines)

for devices in switches:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    # Call each command line by line and send to the switch
    output = net_connect.send_config_set(lines)
    print(output)


