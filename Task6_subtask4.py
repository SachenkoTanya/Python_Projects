def replace_word(file_name, old_word, new_word):
    with open(file_name, 'r', encoding='utf-8') as file_object:
        content = file_object.read()
    new_content = content.replace(old_word, new_word)
    with open(file_name, 'w', encoding='utf-8') as file_object:
        file_object.write(new_content)


def main():
    file_name = 'learning_python.txt'
    old_word = 'Python'
    new_word = 'Java'
    replace_word(file_name, old_word, new_word)
    with open(file_name, 'r', encoding='utf-8') as file_object:
        print(file_object.read())


if __name__ == '__main__':
    main()
