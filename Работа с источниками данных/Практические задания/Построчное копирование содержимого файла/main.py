INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r', encoding='utf-8') as file_1, \
            open(OUTPUT_FILE, 'w', encoding='utf-8') as file_2:
        for i in file_1:
            file_2.write(i.upper())

        # TODO перезаписать содержимое одного файла в другой


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
