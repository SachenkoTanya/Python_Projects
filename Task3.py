# Multiparadigm programming languages,  Task2
# Sachenko Tanya,  IKM-221a

print('Multiparadigm programming languages,  Task2')
print('Sachenko Tanya,  IKM-221a', end='\n\n')

import math

try:
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))

    if b == a:
        raise ValueError("Error: b and a cannot have the same value")
    if b > a:
        raise ValueError("Error: b cannot be greater than a")

    result = math.sqrt((a - b) ** 5 / (b - a) ** 3)
    print(f"Result: {result}")

except ValueError as b_error:
    print("Error with b value:", b_error)