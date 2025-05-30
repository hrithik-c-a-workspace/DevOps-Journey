'''
    Write a generator that alternates between returning Even and Odd
'''

def number_type_generator():
    n = 0
    num_type = ''
    while True:
        n += 1
        if n % 2 == 0:
            num_type = 'Even' 
        else:
            num_type = 'Odd' 

        yield num_type    


number_type = number_type_generator()

print(next(number_type))
print(next(number_type))
print(next(number_type))