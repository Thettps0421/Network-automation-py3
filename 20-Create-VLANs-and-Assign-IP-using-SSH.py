# importing netmiko package library for our code
from netmiko import ConnectHandler
# Createing a dictionary for our perticular device, here the device is Cisco virtual IOS
iosv_12 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.20',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}
# Calling the ConnectHandler Library [**iosv_12 means telling python to consider the contents of the dictionary as key value pairs instead of single elements.]
net_connect = ConnectHandler(**iosv_12)
net_connect.enable()
#Sending a command in to the switch
output = net_connect.send_command("show ip int br")
print(output)
# Create a list that includes all the commands that we need to execute
config_commands = ['int vlan 5', 'ip add 5.5.5.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(10, 20):
    print("Creating VLAN" + str(n))
    config_commands = ['vlan ' + str(n), 'name DevOps_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)

