class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        if not self.available:
            raise Exception('Mentioned book not available !')
        self.available = False
        print(f"You have borrowed the book '{self.title}'.")
    
    def return_book(self):
        if self.available:
            raise Exception('Mentioned book not borrowed, to return !')
        self.available = True
        print(f"Book '{self.title}' returned.")
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def search_book(self, keyword):
        matched_books = [b for b in self.books if keyword.lower() in b.title.lower() or keyword == b.isbn]
        if not matched_books:
            raise Exception('Book not found with the given keyword!')
        return matched_books


lib = Library()
b1 = Book("Daredavil", "Paul Crilley", "1234")
b2 = Book("Iron Man", "Marie Javins", "5678")
b3 = Book("Batman: Year One", "Frank Miller", "9012")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)


try:
    b1.return_book()
except Exception as e:
    print(e)


for book in lib.books:
    print(book.__dict__)

try:
    b2.borrow()
    b2.borrow()  # Raise error: already borrowed
   
except Exception as e:
    print(e)


try:
    found = lib.search_book("Man")
    for book in found:
        print(f"🔍 Found Book:'{book.title}' by{book.author}")
except Exception as e:
    print(e)
