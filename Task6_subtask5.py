def write_guest_book():
    filename = 'guest_book.txt'
    while True:
        name = input('What is your name? ')
        if name == 'quit':
            break
        message = f'Hello, {name}! Thank you for visiting us.\n'
        with open(filename, 'a', encoding='utf-8') as file_object:
            file_object.write(message)
        print(f'Greeting written to {filename}.\n')


if __name__ == '__main__':
    write_guest_book()
