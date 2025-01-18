from typing import List

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """
    Атрибуты:
        id (int): Уникальный идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    """
    def __init__(self, id: int, name: str, pages: int):

        if not isinstance(id, int):
            raise TypeError('id должен быть int')
        if not isinstance(pages, int):
            raise TypeError('pages должен быть int')
        if not isinstance(name, str):
            raise TypeError('name должен быть строкой')

        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги.
        """
        return f"Книга '{self.name}'"

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.
        """
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    """
    Класс, представляющий библиотеку, содержащую список книг.

    Атрибуты:
        book_list (list): Список объектов класса Book в библиотеке.
        last_index (int): Последний использованный идентификатор книги.
    """
    def __init__(self, book_list: list = []) -> None:
        if not isinstance(book_list, List):
            raise TypeError('book должен быть списком')
        
        self.book_list = book_list
        self.last_index = 0
        
    def get_next_book_id(self) -> int:
        """
        Возвращает следующий уникальный идентификатор для книги.

        Если библиотека пуста, возвращает 1. Если книги уже есть, возвращает
        идентификатор на единицу больше максимального id в списке книг.
        """
        if self.book_list == []:
            return self.last_index + 1
        else:
            temp = 0
            for i in range (0, len(self.book_list)):
                if self.book_list[i].id > temp:
                    temp = self.book_list[i].id
            return temp + 1
    
    def get_index_by_book_id(self, search_book_id: int):
        """
        Возвращает индекс книги в списке по её id.

        Параметры:
            search_book_id (int): Идентификатор книги для поиска.
        """
        temp_list = []
        for i in range(0, len(self.book_list)):
            if self.book_list[i].id == search_book_id:
                temp_list.append(i)
        if temp_list == []:
            raise ValueError(f'Книги с запрашиваемым id {search_book_id} не существует')
        else:
            return ' '.join(map(str, temp_list))
                
                
if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    #print('\nПроверяем следующий id для пустой библиотеки:')
    print(empty_library.get_next_book_id())  

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    
    library_with_books = Library(book_list=list_books)  # инициализируем библиотеку с книгами
    
    #print('\nПроверяем следующий id для непустой библиотеки:')
    print(library_with_books.get_next_book_id()) 

    #print('\nпроверяем индекс книги с id = 1:\n')
    print(library_with_books.get_index_by_book_id(1))
