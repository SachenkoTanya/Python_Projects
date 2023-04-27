import re

pattern = r"CHAPTER [IVX]+\s?—\s?[A-Z\s]+"


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


text = read_file("The life and adventures of Alexander Selkirk, the real Robinson Crusoe.txt")
matches = re.findall(pattern, text)
with open("chapters.txt", "w", encoding="utf-8") as file2:
    for match in matches:
        file2.write(match + "\n")
