def book_list_view(library):
    if not library:
        print("Библиотека пуста.")
        return

    print("Список книг:")
    for title in library.keys():
        print(title)


def add_book(library, title, author, year):
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


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена из библиотеки.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def issue_book(library, title):
    if title in library:
        availability = library[title].get("availability")

        if availability is None:
            print(f"Книга '{title}' в библиотеке, но её статус не определён. Сначала уточните статус.")
        elif availability:
            library[title]["availability"] = False
            print(f'Книга "{title}" успешно выдана.')
        else:
            print(f'Книга "{title}" уже выдана.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def return_book(library, title):
    if title in library:
        availability = library[title].get("availability")

        if availability is None:
            print(f"Книга '{title}' в библиотеке, но её статус не определён. Сначала уточните статус.")
        elif not availability:
            library[title]["availability"] = True
            print(f'Книга "{title}" успешно принята обратно.')
        else:
            print(f'Книга "{title}" уже доступна в библиотеке.')
    else:
        print(f'Книги "{title}" нет в библиотеке.')


def find_book(library, title):
    if title in library:
        info = library[title]
        availability = info.get("availability")

        print(f"Название: {title}")
        print(f"Автор: {info['author']}")
        print(f"Год издания: {info['year']}")

        if availability is None:
            print("Состояние доступности: Книга в библиотеке, но её статус не определён")
        elif availability:
            print("Состояние доступности: Книга доступна")
        else:
            print("Состояние доступности: Книга выдана")
    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")


def main_menu():
    library = {
        "1984": {
            "author": "Джордж Оруэлл",
            "year": 1949,
            "availability": None
        },
        "Гарри Поттер и философский камень": {
            "author": "Джоан Роулинг",
            "year": 1997,
            "availability": True
        },
        "Гарри Поттер и Тайная комната": {
            "author": "Джоан Роулинг",
            "year": 1998,
            "availability": False
        }
    }

    while True:
        print("\n=== Меню управления библиотекой ===")
        print("1. Показать список книг")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Выдать книгу")
        print("5. Вернуть книгу")
        print("6. Найти книгу")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ").strip()

        if choice == "1":
            book_list_view(library)
        elif choice == "2":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора: ").strip()
            year = input("Введите год издания: ").strip()
            if not year.isdigit():
                print("Год должен быть числом!")
                continue
            add_book(library, title, author, int(year))
        elif choice == "3":
            title = input("Введите название книги для удаления: ").strip()
            remove_book(library, title)
        elif choice == "4":
            title = input("Введите название книги для выдачи: ").strip()
            issue_book(library, title)
        elif choice == "5":
            title = input("Введите название книги для возврата: ").strip()
            return_book(library, title)
        elif choice == "6":
            title = input("Введите название книги для поиска: ").strip()
            find_book(library, title)
        elif choice == "7":
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 7.")


if __name__ == "__main__":
    main_menu()