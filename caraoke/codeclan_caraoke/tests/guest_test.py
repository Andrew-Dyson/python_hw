import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Phil")

    def test_get_guest_name(self):
        self.assertEqual("Phil", self.guest_1.get_guest_name())
