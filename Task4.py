# Multiparadigm programming languages,  Task2
# Sachenko Tanya,  IKM-221a

print('Multiparadigm programming languages,  Task2')
print('Sachenko Tanya,  IKM-221a', end='\n\n')


def is_prime(max_value):
    if max_value <= 1:
        return False
    for i in range(2, int(max_value ** 0.5) + 1):
        if max_value % i == 0:
            return False
    return True


max_value = int(input("Enter the maximum value to check: "))

for current_number in range(2, max_value + 1):
    mersenne_number = 2 ** current_number - 1
    if is_prime(current_number) and is_prime(mersenne_number):
        print(mersenne_number)
