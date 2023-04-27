def get_the(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    texts = text.split('\n\n')

    for t in enumerate(texts):
        count = t.count('the')
        return count


if __name__ == '__main__':
    input_filename = 'The Project Gutenberg eBook of Historical Vignettes.txt'
    count_the = get_the(input_filename)
    print(f'In the text found {count_the} occurrences of the word "the"')
