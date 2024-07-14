class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, book is not checked out
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def is_checked_out(self):
        return self._is_checked_out
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        else:
            return False  # Book is already checked out
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        else:
            return False  # Book is not checked out


class Library:
    def __init__(self):
        self._books = []  # Initialize an empty list to store books
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                return book.check_out()
        return False  # Book not found or already checked out
    
    def return_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                return book.return_book()
        return False  # Book not found or not checked out
    
    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            return available_books
        else:
            return None  # No available books