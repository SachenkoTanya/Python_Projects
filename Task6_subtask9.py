def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


text = read_file('The life and adventures of Alexander Selkirk, the real Robinson Crusoe.txt')

lowercase_count = 0
uppercase_count = 0

for char in text:
    if char.isalpha() and char.islower():
        lowercase_count += 1
    elif char.isalpha() and char.isupper():
        uppercase_count += 1

total_count = lowercase_count + uppercase_count
lowercase_percent = (lowercase_count / total_count) * 100
uppercase_percent = (uppercase_count / total_count) * 100

print(f"Percentage of lowercase letters: {lowercase_percent}%")
print(f"Percentage of uppercase letters: {uppercase_percent}%")
