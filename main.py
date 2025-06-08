def book_list_view(library):
    if not library:
        print("Библиотека пуста.")
        return

    print("Список книг:")
    for title in library.keys():
        print(title)


def add_book(title, author, year):
    if title in library:
        update = input(f"Книга '{title}' уже существует. Обновить информацию? (yes/no): ").strip().lower()

        if update == 'yes':
            library[title]['author'] = author
            library[title]['year'] = year
            print(f'Информация о книге "{title}" успешно обновлена.')
        else:
            print('Данные остались прежними.')
    else:
        new_book = {"author": author, "year": year, "availability": True}
        library[title] = new_book
        print(f'Книга "{title}" успешно добавлена в библиотеку.')


def remove_book(title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена из библиотеки.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def issue_book(title):
    if title in library:
        if library[title]["availability"]:
            library[title]["availability"] = False
            print(f'Книга "{title}" успешно выдана.')
        else:
            print(f'Книга "{title}" уже была выдана ранее.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def return_book(title):
    if title in library:
        if not library[title]["availability"]:
            library[title]["availability"] = True
            print(f'Книга "{title}" успешно принята обратно.')
        else:
            print(f'Книга "{title}" уже находится в библиотеке.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def find_book(title):
    if title in library:
        info = library[title]
        availability_status = "Доступна" if info["availability"] else "Выдана"
        print(f"Название: {title}")
        print(f"Автор: {info['author']}")
        print(f"Год издания: {info['year']}")
        print(f"Состояние доступности: {availability_status}")
    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")

library = {
    "Гарри Поттер и философский камень": {
        "author": "Джоан Роулинг",
        "year": 1997,
        "availability": True
    },
    "Гарри Поттер и Тайная комната": {
        "author": "Джоан Роулинг",
        "year": 1998,
        "availability": False
    },
    "Гарри Поттер и узник Азкабана": {
        "author": "Джоан Роулинг",
        "year": 1999,
        "availability": True
    }
}

if __name__ == "__main__":
    add_book("Гарри Поттер и Кубок огня", "Джоан Роулинг", 2000)
    add_book("Гарри Поттер и философский камень", "Роулинг Дж.", 1997)
    remove_book("Гарри Поттер и Тайная комната")
    issue_book("Гарри Поттер и философский камень")
    return_book("Гарри Поттер и философский камень")
    find_book("Гарри Поттер и философский камень")
    find_book("Дневники вампира")

    book_list_view(library)