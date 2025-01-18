class Book:
    def __init__(self, id, name, pages):
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
        return f"Книга '{self.name}'"

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"

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

if __name__ == '__main__':
    
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    
    #print("\nПроверяем метод __str__ \n")
    for book in list_books:
        print(book) 

    #print("\n\nПроверяем метод __repr__ \n")
    print(list_books)
