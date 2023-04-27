def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_object:
        lines = file_object.readlines()
    return lines


if __name__ == '__main__':
    name_file = "learning_python.txt"
    Lines = read_file(name_file)
    for line in Lines:
        print(line.rstrip())
