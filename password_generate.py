import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
special_characters = '!@#$%^&*()_+'

Use = lower_case + upper_case + number + special_characters
length = 8

password = ''.join(random.sample(Use, length))

print('Your password is: ', password)
