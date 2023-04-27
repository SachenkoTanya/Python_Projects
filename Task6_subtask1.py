def read_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        numbers = list(map(int, f))
    return numbers


def compute_sum(numbers):
    result = sum(numbers)
    return result


def print_sum(result):
    print('Sum of numbers:', result)


def write_sum(result, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(result))


def main():
    numbers = read_numbers('numbers.txt')
    result = compute_sum(numbers)
    print_sum(result)
    write_sum(result, 'sum_numbers.txt')


if __name__ == '__main__':
    main()
