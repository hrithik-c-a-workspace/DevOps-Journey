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
    
    print('Please enter a valid name.')
    return False

def normalised_input(value=''):
    return " ".join(str(value).split()) 

def default_helper():
    return True

def get_input(prompt='', helperFunction = default_helper):
    entered_value = input(f'{prompt}: ').strip()
    if input_validator(value=entered_value) and helperFunction(entered_value):
        final_value = normalised_input(entered_value) if input_validator(value=entered_value) else None
        return final_value
    return None

input_name = get_input('Enter a name', helperFunction=name_validator)

if input_name is not None:
    print(f'The name you have entered is: {input_name}')
