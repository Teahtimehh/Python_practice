library = {}

def book_list_view(library):
    if not library:
        print("Библиотека пуста.")
    else:
        print("Список книг:")
        for title in library.keys():
            print(title)


library["Гарри Поттер и философский камень"] = {"author": "Джоан Роулинг", "year": 1997, "availability": True}
library["Гарри Поттер и Тайная комната"] = {"author": "Джоан Роулинг", "year": 1998, "availability": False}
library["Гарри Поттер и узник Азкабана"] = {"author": "Джоан Роулинг", "year": 1999, "availability": True}

book_list_view(library)