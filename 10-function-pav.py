# Passing argument values in a function.

def calc(v1, v2):
    print('addition         :', v1 + v2)
    print('multiplication   :', v1 * v2)
    print('division         :', v1 / v2)
    print('subtraction      :', v1 - v2)

a = input('Enter the first number   :')
b = input('Enter the Second number  :')
#c = input('Enter the Third number  :')
calc(int(a), int(b))