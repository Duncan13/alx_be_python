class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __repr__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __repr__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self, books):
        self.books = []
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Can only add instances of Book, EBook or PrintBook")
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            print(book)