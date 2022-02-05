
#Using fstrings instead of variables and pluses in strings

my_value= 2.345

print("my value =", my_value)

#instead use f-strings
the_string=f'my_value = {my_value}'
print(the_string)

#or simpler
the_string=f'{my_value = }'
print(the_string)

### Formaters
#You can format the value before saving or printing

#Date:
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
print(f'{now=:%Y-%m-%d}')

#Float with decimals instead of round
print(f'{my_value=:.2f}')

#or even using nested_formatting:
nested_format=".2f"
print(f'{my_value=:{nested_format}}')
