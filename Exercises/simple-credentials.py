'''
    This is a simple credentials programs that helps to understand concept of continue statement.
'''

print('Hello user, Enter your credentials. \n')

while True:
    username = input('Username: ')
    if(username != 'bruce_wayne'):
        continue

    print("Enter your password to continue. Hint: It's your catchphrase!")

    print("Something in the way")
    for i in range(3):
         print("mmm 🎶")

    print('Who are you?')

    password =input('Password: ')
    if(password == "iambatman"):
        break

print('Access Granted.')
