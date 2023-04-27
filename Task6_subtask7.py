def format_file(file_name, formatted_text_file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        formatted_text = text.replace('\n', ' ')
        with open(formatted_text_file_name, 'w', encoding='utf-8') as formatted_file:
            formatted_file.write(formatted_text)
            return 'Formatting complete'


if __name__ == '__main__':
    name_file = 'Emmanuel Burden, merchant of Thames ' \
                'st in the city of London, exporter of hardware.txt'
    formatted_text_file = 'format_text.txt'
    print(format_file(name_file, formatted_text_file))
