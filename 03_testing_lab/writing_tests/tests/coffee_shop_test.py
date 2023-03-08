import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("Skye's Coffe Shop", 100.00)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Skye's Coffe Shop", self.coffee_shop.name)

    def test_can_increase_till(self):
        self.coffee_shop.increase_till(5.99)
        excepted = 105.99
        actual = self.coffee_shop.till
        self.assertEqual(excepted, actual)
        # self.assertEqual(105.99, self.coffee_shop.till)