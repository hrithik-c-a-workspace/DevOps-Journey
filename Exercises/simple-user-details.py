'''
    Write a Python program that takes a name, age as an argument and prints the name and age.
'''
import re

# Reusable functions
def show_output(message='', value=None):
    if value is not None:
        print(f'{message} {value}')

def input_validator(value=''):
    if not value.strip():
        show_output(message='Input cannot be empty.', value='\n')
        return False
    return True

def name_validator(value=''):
    pattern = r"^[A-Z][a-zA-Z\s\-]*$"
    if re.fullmatch(pattern=pattern, string=value):
        return True

    show_output(message='Please enter a valid name.', value='\n')
    return False

def age_validator(value=''):
    if int(value) > 0:
        return True
    
    show_output(message='Please enter a valid age.', value='\n')
    return False

def normalised_input(value=''):
    return " ".join(str(value).split()) 

def default_helper():
    return True


def get_input(prompt='', helperFunction = default_helper):
    entered_value = input(f'{prompt}: ').strip()
    if input_validator(value=entered_value) and helperFunction(entered_value):
        final_value = normalised_input(entered_value)
        return final_value
    return None

# Main
input_name = get_input('Enter your name', helperFunction=name_validator)
if input_name is not None:
    show_output(message="It's great to meet you,", value=f"{input_name}! \n")

input_age = get_input('Enter your age', helperFunction=age_validator)
if input_age is not None:
    get_next_age = lambda age: str(age + 1)
    show_output(message="Congrats. In the next year you'll be", value=f"{get_next_age(int(input_age))}. \n")


    

