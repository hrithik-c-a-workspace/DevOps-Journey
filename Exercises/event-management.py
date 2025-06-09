'''
    This program is to learn concepts of Truthy and Falsey values.
'''

name = ''
while not name:
    name = input('Enter your name: ')

no_of_guests = input('Enter the number of guests (0 if none): ')
if no_of_guests:
    print('Be sure to have enough room for all your guests.')

print('Done.')