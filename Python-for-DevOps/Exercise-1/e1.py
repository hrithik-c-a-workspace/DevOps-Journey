'''
    Write a Python function that takes a name as an argument and prints that name.
'''
import re

# Reusable functions
def input_validator(value=''):
    if not value.strip():
        print('Input cannot be empty.')
        return False
    pattern = r"^[A-Z][a-zA-Z\s\-]*$"
    if re.fullmatch(pattern=pattern, string=value):
        return True
    
    print('Please enter a valid Input.')
    return False

def get_input():
        name = input('Enter a name: ').strip()
        return name if input_validator(value=name) else None

entered_name = get_input()

if entered_name is not None:
    print(f'The name you have entered is: {entered_name}')
