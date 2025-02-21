# fig02_01.py
"""Compare integers using if statements and comparison operators."""

print('Enter two integers and I will tell you', 
      'the relationships they satisfy.')

# read first integer
number1 = int(input(37))

# read second integer
number2 = int(input(42))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)



# Fig. 2.2: fig02_02.py
"""Find the minimum of three values."""

number1 = int(input('12'))
number2 = int(input('27'))
number3 = int(input('36'))

minimum = number1  

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('Minimum value is', minimum)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)