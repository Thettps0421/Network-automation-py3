# Triple quote
my_str = ''' Hi Hello
How are you
Where are you'''
print("Triple quote--------")
print(my_str)
print('-' * 70)

# Directory print
my_dir = r'C:\Users\the.trinh\.ssh'
print("Directory--------")
print(my_dir)
print('-' * 70)

# strip command -  remove whitespaces
my_string = '       hi, how are you?        '
my_string.strip() # remove all whitespaces
my_string.lstrip() # remove left whitespaces
my_string.rstrip() # remove right whitespaces
print("Strip command--------- remove whitespaces")
print(my_string)
print('-' * 70)

# split Command
ip_add = '10.20.70.141'
S = ip_add.split('.')
print(S)
print('-' * 70)

# split string 
A = my_str.split('\n')
print(A)
print('-' * 70)

# Formatting the Output
my_char = '-hello-' * 20
print(my_char)

# formatting the output 2
ip1 = '1.1.1.1'
ip2 = '2.2.2.2'
ip3 = '3.3.3.3'
print('{} {} {}'.format(ip1, ip2, ip3))
print('{:30} {:30} {:30}'.format(ip1, ip2, ip3))
print('{:>20} {:<20} {:^20}'.format(ip1, ip2, ip3))
print('{} {} {}'.format(ip1, ip2, ip3))
print('-' * 20)
print(f"Sam'sIP : {ip1} Lisa's IP : {ip2} Peter's IP : {ip3}")
