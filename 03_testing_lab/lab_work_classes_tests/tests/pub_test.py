import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("cider", 3.50)
        self.drink_2 = Drink("wine", 7.00)
        self.drink_3 = Drink("cocktail", 15.00)
        self.pub = Pub("Edinburgh Arms", 100, [self.drink_1, self.drink_2, self.drink_3])
        self.customer = Customer("David", 70)

    def test_count_drinks(self):
        self.assertEqual(3, self.pub.count_drinks())

    def test_pub_has_name(self):
        self.assertEqual("Edinburgh Arms", self.pub.name)

    def test_pub_sell_drink(self):
        self.pub.sell_drink(self.customer, self.drink_1)

        # check customer has drink
        self.assertEqual(1, self.customer.count_drinks())

        # check pub has fewer drinks
        self.assertEqual(2, self.pub.count_drinks())

        # check till has extra money
        self.assertEqual(103.5, self.pub.till)

        # check customer has less money
        self.assertEqual(66.5, self.customer.count_wallet())