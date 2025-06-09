'''
    This is a program that helps to understand the concept of break statement.
'''

number = None

while True:
    try:
        number = int(input('Enter the number 100 to exit the Loop: '))
        if(number == 100):
            break
    except ValueError:
        print('Enter a vaild number. \n')
        
print('Thank you!')