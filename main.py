class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
        
    @property
    def author(self):
        """ Возвращает автора книги. """
        return self._author
        
    @property
    def name(self):
        """ Возвращает название книги. """
        return self._name

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
 

class PaperBook(Book):
    """ Класс для бумажных книг. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        
        if not isinstance(pages, int):
            raise TypeError('pages должен быть int')
        
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. {self.pages} страниц"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Класс для аудиокниг. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        
        if not isinstance(duration, (int, float)):
            raise TypeError('duration должен быть int или float')
        
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. {self.duration} минут"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

if __name__ == '__main__':
    book_1 = Book('book_1', 'author_1')
    print(repr(book_1))

    paper_book = PaperBook('name', 'name', 20)
    print(repr(paper_book))
    
    paper_book._name = 10
    print(paper_book)
    
    # audio_book = AudioBook('name', 'name', "2")
    # print(audio_book)