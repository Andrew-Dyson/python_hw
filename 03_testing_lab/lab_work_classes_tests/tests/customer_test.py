import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Murray", 50)

    def test_customer_has_name(self):
        self.assertEqual("Murray", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_add_drink_customer(self):
        drink_bought = Drink("Long Island", 10.99)
        self.customer.add_drink(drink_bought)
        self.assertEqual(1, self.customer.count_drinks())

    