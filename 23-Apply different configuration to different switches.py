# Remove the VLANs 11 to 15 from all the switches.
# And configure a new VLAN_25 interface (SVI) only on Switches3(SW3) and assign it on gig2/0
# So we need to create a configuration file for all the switches. then we need to create another configuration file exclusively for Switche3. 
#--> Call these files separately in the python code and that is how we can bale to achieve our goal

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

with open('all_switches.txt') as f:
    lines = f.read().splitlines()
print(lines)

for devices in switches:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)

with open('switch_3.txt') as f:
    lines = f.read().splitlines()
print(lines)

net_connect = ConnectHandler(**switch3)
net_connect.enable()
output = net_connect.send_config_set(lines)
print(output)