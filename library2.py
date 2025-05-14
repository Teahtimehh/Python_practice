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


def book_list_view(library):
    if not library:
        print("Библиотека пуста.")

    print("Список книг:")
    for title in library.keys():
        print(title)


book_list_view(library)