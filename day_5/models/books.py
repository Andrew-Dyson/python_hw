from models.book import Book

book_1 = Book("Excursion guide to the geology of arran", "Murray Macgregor", "Natural science guide book", True)
book_2 = Book("The geology of the yorkshire coast", "Peter Rawson", "Natural science guide book", False)
book_3 = Book("Exploring the geology on the isle of arran", "C J Nicholas", "Natural science guide book", True)

book_list = [book_1, book_2, book_3]

def add_book(book):
    book_list.append(book)

# def remove_book(book):
#     book_list.remove(book)

def remove_book(book):
    book_list.pop(book)

def check_out_book(book):
    book.checked_out = True