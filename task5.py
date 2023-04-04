import math


def get_number(message, expected_type=float):
    user_input = input(message)
    try:
        converted_input = expected_type(user_input)
        return converted_input
    except ValueError:
        print(f'The value must be of type {expected_type.__name__}')
        return get_number(message, expected_type)


# 1 part

# Initialize variables
n = 1
row_sum = 0

# Calculation of the sum of the first 13 members of the series
while n <= 13:
    an = math.log(math.factorial(n)) / (n ** 2)
    row_sum += an
    n += 1

# Display the result
print(f'The sum of the first 13 members of the series: {row_sum}')

# 2 part
n = get_number('Enter an integer: ', int)
count = int(math.log10(n)) + 1
print(f'The sum of the first 13 members of the series: {count}')

# 3 part
n = get_number('Enter a number: ', float)
x = n
E = 1e-4
while abs(x * x - n) > E:
    x = (x + n / x) / 2
print('The square root of a number', n, 'is equal to', x)
