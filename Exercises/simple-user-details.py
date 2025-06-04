'''
    Write a Python function that takes a name as an argument and prints that name.
'''
import re

# Reusable functions
def input_validator(value=''):
    if not value.strip():
        print('Input cannot be empty.')
        return False
    return True

def name_validator(value=''):
    pattern = r"^[A-Z][a-zA-Z\s\-]*$"
    if re.fullmatch(pattern=pattern, string=value):
        return True
    
    print('Please enter a name.')
    return False

def normalised_input(value=''):
    return " ".join(value.split())  

def get_input():
    name = input('Enter a name: ').strip()
    if input_validator(value=name):
        entered_name = normalised_input(name) if input_validator(value=name) else None
        return { name: entered_name }
    return None

entered_values = get_input()

if entered_values is not None:
    print(f'The name you have entered is: {entered_values['name']}')
