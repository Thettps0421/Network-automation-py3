# Dictionaties
switch = {'cisco': '4500',
'ip': '1.1.1.1',
'location': 'Sai Gon'}
print(switch)
switch['serial number'] = 'ABCD1234'
print(switch)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)

# Conditions
value1 = input("Enter a value.10 or 20 or 30 :")
if value1 == '10':
    print("Value is 10")
elif value1 == '20':
    print("value is 20")
else:
    print("value is 30")
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)
# Elif condition
value2 = input("Enter a value.10 or 20 or 30 :")
value2 = int(value2) # string value is converted to Integer here
if value2 == 10:
    print("value is 10")
elif value2 == 20:
    print("value is 20")
else:
    print("value is 30")
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)