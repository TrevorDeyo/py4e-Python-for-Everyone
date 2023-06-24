import re

user_input = input('Input File Path: ')

with open(user_input, 'r') as file:
    text = file.read()

numbers = re.findall(r'\d+', text)

total = sum(map(int, numbers))
print(total)