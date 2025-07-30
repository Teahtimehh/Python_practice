from pathlib import Path
import os

print("1. Чтение файла data.txt:")
with open('data.txt', 'r', encoding='cp1251', errors='replace') as file:
    content = file.read()
    print(content)

print("\n2. Добавление новых строк в файл...")
new_lines = [
    "\nДополнительная строка 1",
    "Дополнительная строка 2",
    "Дополнительная строка 3"
]

with open('data.txt', 'a', encoding='cp1251', errors='replace') as file:
    for line in new_lines:
        file.write(line + '\n')

print("\n3. Построчное чтение файла:")
with open('data.txt', 'r', encoding='cp1251', errors='replace') as file:
    for line_num, line in enumerate(file, 1):
        print(f"Строка {line_num}: {line.strip()}")

print("\n4. Копирование файла в бинарном режиме...")
try:
    with open('data.txt', 'rb') as src_file:
        with open('data_copy.txt', 'wb') as dst_file:
            while True:
                chunk = src_file.read(1024)
                if not chunk:
                    break
                dst_file.write(chunk)
    print("Файл успешно скопирован как data_copy.txt")
except Exception as e:
    print(f"Ошибка при копировании: {e}")