import unittest
from models.book import Book
from models.books import *


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("excursion guide to the geology of arran", "murray macgregor", "natural science guide book", True)
        self.book_2 = Book("the geology of the yorkshire coast", "peter rawson", "natural science guide book", False)
        self.book_3 = Book("exploring the geology on the isle of arran", "c j nicholas", "natural science guide book", True)
        self.book_list = [self.book_1, self.book_2, self.book_3]


    def test_book_has_a_name(self):
        self.assertEqual("excursion guide to the geology of arran", self.book_1.get_book_name())

    def test_book_has_an_author(self):
        self.assertEqual("peter rawson", self.book_2.get_book_author())

    def test_book_has_a_genre(self):
        self.assertEqual("natural science guide book", self.book_3.get_book_genre())

    def test_can_add_book(self):
        book_4 = Book("geology of scotland", "a geologist", "nature books", True)
        add_book(book_4)
        self.assertEqual(4, len(book_list))

    def test_can_remove_book(self):
        book_4 = Book("geology of scotland", "a geologist", "nature books", True)
        add_book(book_4)
        remove_book(3)
        self.assertEqual(3, len(self.book_list))

    def test_can_check_out_book(self):
        book_4 = Book("geology of scotland", "a geologist", "nature books", False)
        check_out_book(book_4)
        self.assertEqual(True, book_4.checked_out)