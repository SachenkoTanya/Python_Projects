def read_number():
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Please provide an integer')
        return read_number()
    return number


def check_parity(number):
    if number % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return parity


def write_to_file(number, parity):
    with open('number_parity.txt', 'w', encoding='utf-8') as f:
        f.write(f'The number {number} is {parity}.')


def main():
    number = read_number()
    parity = check_parity(number)
    write_to_file(number, parity)


if __name__ == '__main__':
    main()
