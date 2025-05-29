'''
Write a python function that takes a string as an argument and prints whether
it is upper- or lowercase.
'''

def string_case_checker(value=''):
    if not value.strip():
        print('Input cannot be empty.')
        return

    cases = {
        'upper': False,
        'lower': False
    }
    if value.isupper():
        cases['upper'] = True
    elif value.islower(): 
        cases['lower'] = True

    for key, value in cases.items():
        if value is True:
            return key
    return    

def get_input():
    string = input('Enter a string: ').strip()
    case = string_case_checker(string)  
    return [string, case] if case is not None else None

entered_string = get_input()    

if entered_string is not None:
    print(f'The string {entered_string[0]} you have entered is {entered_string[1]} case.')  