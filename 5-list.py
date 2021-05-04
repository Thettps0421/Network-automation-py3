sample_list = ['IP Address', 80 , 44.20]
x = sample_list.append('Port Number')
print(sample_list)
print(x)
print(sample_list.count(80))
print(sample_list.pop(0))
print(sample_list.remove(44.20))
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)
f = open(r'C:\Users\the.trinh\Documents\Pip Installation\ios_status.txt')
data = f.readlines()
data[0:4]
data2 = data[5:7]
print(data)
print(data2)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)

n = open(r'C:\Users\the.trinh\Documents\Pip Installation\sw1.txt')
ndata = n.readlines()
ndata[0:4]
ndata2 = ndata[7:11]
print(ndata)
print(ndata2)
print('-' * 60)
print('----------Finished-----------')
print('''

''')
print('-' * 20 + ' Start ' + '-' * 20)
# Join Operation
my_ip = '10.20.30.141'
split = my_ip.split('.')
print(f'"Split IP:"{split}')
print(f'"Join IP: "{".".join(split)}')
