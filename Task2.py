# Multiparadigm programming languages,  Task2
# Sachenko Tanya,  IKM-221a

print('Multiparadigm programming languages,  Task2')
print('Sachenko Tanya,  IKM-221a', end='\n\n')


def get_float_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid number!")


INPUT_MESSAGE = 'Input  {}  please: '
x = get_float_input(INPUT_MESSAGE.format('x'))
y = get_float_input(INPUT_MESSAGE.format('y'))
z = get_float_input(INPUT_MESSAGE.format('z'))

if x == -11.3 or z == 11.3:
    raise Exception('Error!!!')
else:
    result = (x / (x + 11.3)) + (y / (z - 11.3))
    print(f"Result: {result}")
