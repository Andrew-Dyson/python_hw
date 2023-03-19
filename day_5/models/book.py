class Book():
    def __init__(self, title, author, genre, checked_out):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out

    def get_book_name(self):
        return self.title
    
    def get_book_author(self):
        return self.author
    
    def get_book_genre(self):
        return self.genre
    
    