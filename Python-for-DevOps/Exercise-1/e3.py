'''
Write a list comprehension that results in a list of every letter in the word smogether captialized.
'''

word= 'smogether'

capitalized_letters = [l.upper() for l in word]

print(capitalized_letters)