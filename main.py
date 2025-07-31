from pathlib import Path
import os


def read_file_content():
    try:
        with open('data.txt', 'r', encoding='cp1251', errors='replace') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл data.txt не найден"


def append_to_file(lines):
    with open('data.txt', 'a', encoding='cp1251', errors='replace') as file:
        for line in lines:
            file.write(line + '\n')


def read_file_line_by_line():
    try:
        with open('data.txt', 'r', encoding='cp1251', errors='replace') as file:
            for line_num, line in enumerate(file, 1):
                yield f"Строка {line_num}: {line.strip()}"
    except FileNotFoundError:
        yield "Файл data.txt не найден"


def copy_file_binary():
    try:
        with open('data.txt', 'rb') as src_file, open('data_copy.txt', 'wb') as dst_file:
            while True:
                chunk = src_file.read(1024)
                if not chunk:
                    break
                dst_file.write(chunk)
        return "Файл успешно скопирован как data_copy.txt"
    except Exception as e:
        return f"Ошибка при копировании: {e}"


def main():
    print("1. Содержимое файла data.txt:")
    print(read_file_content())

    new_lines = [
        "\nДополнительная строка 1",
        "Дополнительная строка 2",
        "Дополнительная строка 3"
    ]
    append_to_file(new_lines)

    print("\n2. Построчное чтение файла:")
    for line in read_file_line_by_line():
        print(line)

    print("\n3. Копирование файла:")
    print(copy_file_binary())


if __name__ == "__main__":
    main()