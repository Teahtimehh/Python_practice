def book_list_view(library):
    if not library:
        print("Библиотека пуста.")
        return
    print("Список книг:")
    for title in library:
        print(title)


def add_book(library, title, author, year):
    if title in library:
        update = input(f"Книга '{title}' уже существует. Обновить информацию? (yes/no): ").strip().lower()
        if update == 'yes':
            library[title].update({"author": author, "year": year})
            print(f'Информация о книге "{title}" обновлена.')
        else:
            print('Изменения отменены.')
    else:
        library[title] = {"author": author, "year": year, "availability": None}
        print(f'Книга "{title}" добавлена.')


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" удалена.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def issue_book(library, title):
    if title not in library:
        print(f'Книги "{title}" нет в библиотеке.')
        return

    availability = library[title].get("availability")
    if availability is None:
        print(f'Статус книги "{title}" не определён. Сначала установите статус.')
    elif availability:
        library[title]["availability"] = False
        print(f'Книга "{title}" выдана.')
    else:
        print(f'Книга "{title}" уже выдана.')


def return_book(library, title):
    if title not in library:
        print(f'Книги "{title}" нет в библиотеке.')
        return

    availability = library[title].get("availability")
    if availability is None:
        print(f'Статус книги "{title}" не определён. Сначала установите статус.')
    elif not availability:
        library[title]["availability"] = True
        print(f'Книга "{title}" возвращена.')
    else:
        print(f'Книга "{title}" уже доступна.')


def find_book(library, title):
    if title not in library:
        print(f'Книга "{title}" не найдена.')
        return

    book = library[title]
    status = (
        "не определён" if book.get("availability") is None
        else "доступна" if book["availability"]
        else "выдана"
    )
    print(
        f"Название: {title}\n"
        f"Автор: {book['author']}\n"
        f"Год: {book['year']}\n"
        f"Статус: {status}"
    )


def main_menu():
    library = {
        "1984": {"author": "Джордж Оруэлл", "year": 1949, "availability": None},
        "Гарри Поттер и философский камень": {"author": "Дж. Роулинг", "year": 1997, "availability": True},
    }

    menu_actions = {
        "1": lambda: book_list_view(library),
        "2": lambda: add_book(
            library,
            input("Название книги: ").strip(),
            input("Автор: ").strip(),
            int(input("Год издания: ")) if input("Год издания: ").strip().isdigit() else None
        ),
        "3": lambda: remove_book(library, input("Название книги для удаления: ").strip()),
        "4": lambda: issue_book(library, input("Название книги для выдачи: ").strip()),
        "5": lambda: return_book(library, input("Название книги для возврата: ").strip()),
        "6": lambda: find_book(library, input("Название книги для поиска: ").strip()),
        "7": lambda: exit("Выход из программы."),
    }

    while True:
        print("\n" + "=" * 20)
        print("1. Список книг\n2. Добавить книгу\n3. Удалить книгу\n4. Выдать книгу\n5. Вернуть книгу\n6. Найти книгу\n7. Выход")
        choice = input("Выберите действие: ").strip()

        if choice in menu_actions:
            menu_actions[choice]()
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
