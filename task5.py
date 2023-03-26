import math


# 1 part

# Initialize variables
N = 1
SUM = 0

# Calculation of the sum of the first 13 members of the series
while N <= 13:
    an = math.log(math.factorial(N)) / (N ** 2)
    SUM += an
    N += 1

# Display the result
print('The sum of the first 13 members of the series: ', SUM)


# 2 part
while True:
    try:
        N = int(input('Enter an integer: '))
        count = int(math.log10(N)) + 1
        print('The number of digits in the entered number:', count)
        break
    except ValueError:
        print('You entered the wrong value!')


# 3 part
while True:
    try:
        N = float(input('Enter a number: '))
    except ValueError:
        print('You entered the wrong value!')
    else:
        x = N
        E = 1e-4
        while abs(x * x - N) > E:
            x = (x + N / x) / 2
        print('The square root of a number', N, 'is equal to', x)
        break
