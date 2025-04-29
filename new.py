class Book:
    def __init__(self, title, author, ispn, available=True):
        self.title = title
        self.author = author
        self.ispn = ispn
        self.available = available
    def display_info(self):
        print(f"Title: {self.title} \n Author: {self.author} \n ISPN: {self.ispn} \n  Availability: {self.available}")
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if book.available == True:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is not available for borrowing.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")