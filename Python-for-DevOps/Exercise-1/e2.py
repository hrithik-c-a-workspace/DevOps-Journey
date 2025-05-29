'''
Write a python function that takes a string as an argument and prints whether
it is upper- or lowercase.
'''

def string_case_checker(value=''):
    if len(value) == 0:
        print('Input cannot be empty.')
        return
    
    if not value.isalpha():
        print('Invalid Input')
        return

    if value.isupper():
        return 'upper'
    elif value.islower(): 
        return 'lower'
    elif any(c.isupper() for c in value) and any(c.islower() for c in value):
        return 'mixed'
    
    return

def get_input():
    string = input('Enter a string: ').strip()
    case = string_case_checker(string)  
    return [string, case] if case is not None else None

entered_string = get_input()    

if entered_string is not None:
    print(f'The string {entered_string[0]} you have entered is {entered_string[1]} case.')  