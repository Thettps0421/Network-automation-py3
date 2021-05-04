# Loops
my_list = [1, 2, 3, 4]
for i in my_list:
    print("value is: ", i)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)

ip_list = ['192.168.1.1', '192.168.20.30', '10.10.10.30']
for i1 in ip_list:
    print("IP list: ", i1)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)
# print number 0 to 9 using for loop
for i3 in range(10):
    print(i3)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)
# Break for loop
ip_list2 =['192.168.1.1', '192.168.20.30', '10.10.10.30'] 
for ip in ip_list2:
    print("IP is", ip)
    if ip == '192.168.20.30':
            